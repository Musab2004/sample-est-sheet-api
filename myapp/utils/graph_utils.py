import operator
from typing import Annotated, Sequence, TypedDict, List


import pandas as pd
from tabulate import tabulate


from langchain_core.messages import BaseMessage, ToolMessage
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter
from langchain.schema.document import Document


from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import ToolInvocation


from .chains import (
    qa_pair_generator_chain,
    phase_extractor_chain,
    feature_extractor_chain,
    paraphrase_chain,
)


class GraphState(TypedDict):
    project_phases: str
    feedback: str
    file: str
    doc_content: str
    estimation_table: str
    suggestions: str
    questions: List[str]
    phase_questions: List[str]
    qa_pair: str


def show_table(est_sheet):
    df = pd.DataFrame([vars(req) for req in est_sheet])
    return df


def merge_tables(phase_list, feature_list):
    est_table = []
    for phase in phase_list:
        est_table.append(phase)
        if phase.features == "Development Phase":
            phase.sub_functionality_of_features = []
            phase.UI_pages = []
            for feat in feature_list:
                est_table.append(feat)
    return est_table


def get_text_chunks_langchain(text):
    text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=100)
    docs = [Document(page_content=x) for x in text_splitter.split_text(text)]
    return docs


def map_reduce(content):
    output = paraphrase_chain.invoke({"requirement_document": content})
    return output


def processor_node(state):
    print("in processor node")
    file_content = state["file"]

    def count_tokens(text):
        return len(text.split())

    token_count = count_tokens(file_content)
    if token_count > 1000:
        file_content = map_reduce(file_content)
    state["doc_content"] = file_content
    return state


def convert_to_array(qa_pairs):
    new_array = []
    for qa_pair in qa_pairs:
        new_array.append(qa_pair.answer)
    return new_array


def qa_pair_generator_feature(state):
    print("in qa pair node")
    state["qa_pair"] = qa_pair_generator_chain.invoke(
        {
            "requirement_document": state["doc_content"],
            "user_queries": state["questions"],
        }
    ).qa_pair
    state["qa_pair"] = convert_to_array(state["qa_pair"])
    return state


def qa_pair_generator_phase(state):
    print("in qa pair node")
    state["qa_pair"] = qa_pair_generator_chain.invoke(
        {
            "requirement_document": state["doc_content"],
            "user_queries": state["phase_questions"],
        }
    ).qa_pair
    state["qa_pair"] = convert_to_array(state["qa_pair"])
    return state


def feature_extractor(state):
    print("in feature extractor")
    feature_list = feature_extractor_chain.invoke(
        {"user_queries": state["qa_pair"]}
    ).features_list
    state["estimation_table"] = merge_tables(state["estimation_table"], feature_list)
    return state


def phase_extractor(state):
    state["estimation_table"] = phase_extractor_chain.invoke(
        {"project_phases": state["project_phases"], "user_queries": state["qa_pair"]}
    ).phase_list
    return state


def human_feedback(state):
    pass


def should_continue(state):
    if state["feedback"] == "":
        return "end"
    else:
        return "continue"


workflow = StateGraph(GraphState)
workflow.add_node("processor_node", processor_node)
workflow.add_node("phase_extractor", phase_extractor)
workflow.add_node("qa_pair_generator_phase", qa_pair_generator_phase)
workflow.add_node("qa_pair_generator_feature", qa_pair_generator_feature)
workflow.add_node("feature_extractor", feature_extractor)
workflow.add_node("human_feedback_1", human_feedback)


workflow.add_edge(START, "processor_node")
workflow.add_edge("processor_node", "qa_pair_generator_phase")
workflow.add_edge("qa_pair_generator_phase", "phase_extractor")
workflow.add_edge("phase_extractor", "qa_pair_generator_feature")
workflow.add_edge("qa_pair_generator_feature", "human_feedback_1")
workflow.add_edge("human_feedback_1", "feature_extractor")
workflow.add_edge("feature_extractor", "human_feedback_1")


app = workflow.compile(checkpointer=MemorySaver(), interrupt_after=["human_feedback_1"])
