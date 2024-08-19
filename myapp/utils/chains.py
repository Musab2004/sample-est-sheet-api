import operator
import getpass
import os

from dotenv import load_dotenv
from typing import Annotated, Sequence, TypedDict, List
from pydantic import BaseModel, Field

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import (
    BaseModel as CoreBaseModel,
    Field as CoreField,
    validator,
)
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage

from .util_var import (
    phase_template,
    feature_template,
    qa_pair_template,
    fix_array_template,
    paraphrase_template,
)


from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

output_parser = StrOutputParser()

prompt = PromptTemplate(
    template=paraphrase_template,
    input_variables=["requirement_document"],
)

model = ChatOpenAI(temperature=0, model="gpt-4o-mini")

paraphrase_chain = prompt | model | output_parser


class Answers(BaseModel):
    answers: List[str] = Field(..., description="A list of Answers")


parser = PydanticOutputParser(pydantic_object=Answers)
prompt = PromptTemplate(
    template=fix_array_template,
    input_variables=["answers"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

model = ChatOpenAI(temperature=0, model="gpt-4o-mini")

fix_array_chain = prompt | model | parser


class Modules_description(BaseModel):
    modules: List[str] = Field(
        ..., description="It should contain the module name and its description"
    )


class QAItem(BaseModel):
    answer: str = Field(
        ...,
        description="The answer or additional information regarding the feature or use case. Include any details that are missing or need clarification from the client.",
    )


class QAPair(BaseModel):
    qa_pair: List[QAItem] = Field(
        ...,
        description="A list of QAItem objects, where each item represents a question and its corresponding answer related to the feature or use case.",
    )


parser = PydanticOutputParser(pydantic_object=QAPair)
prompt = PromptTemplate(
    template=qa_pair_template,
    input_variables=["requirement_document", "user_queries"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


class feature(BaseModel):
    features: str = Field(
        description="This will require name of the phase that will be needed for the application development"
    )
    sub_functionality_of_features: List["str"] = Field(
        description="It will include the sub functionality it will require for its complete implemenation. try to add all possible subfunctionality any kind of third party integartions etc"
    )
    UI_pages: List["str"] = Field(
        description="It will include the all the frontend pages we need to make these models. Try to cover every sub functionality in these front-end pages"
    )
    assumption: str = Field(
        descripion="make assumption about how it will be implemented and what technologies or third party requirement we will be needing"
    )
    backend_engineer: int = Field(
        ...,
        description="Number of backend engineer is assigned to work on this feature. Example: '0','1','2'etc.",
    )

    frontend_engineer: int = Field(
        ...,
        description="NUmber of  frontend engineer is assigned to work on this feature. Example: '0','1', '2' etc.",
    )

    QA: int = Field(
        ...,
        description="Number of QA engineer is assigned to test this feature. Example: '0','1','2'.",
    )
    AI_Engineer: int = Field(
        ...,
        description="Number of AI engineer needed if there is any task related to AI. Example: '0','1','2'.",
    )


class phase_list(BaseModel):
    phase_list: List[feature]


class feature(BaseModel):
    features: str = Field(
        description="The specific features or use cases discussed by the client in the estimation sheet"
    )
    sub_functionality_of_features: List["str"] = Field(
        description="It will include the sub functionality it will require for its complete implemenation. try to add all possible subfunctionality any kind of third party integartions etc"
    )
    UI_pages: List["str"] = Field(
        description="It will include the all the frontend pages we need to make these models. Try to cover every sub functionality in these front-end pages"
    )
    assumption: str = Field(
        descripion="make assumption about how it will be implemented and what technologies or third party requirement we will be needing"
    )
    backend_engineer: int = Field(
        ...,
        description="Number of backend engineer is assigned to work on this feature. Example: '0','1','2'etc.",
    )

    frontend_engineer: int = Field(
        ...,
        description="NUmber of  frontend engineer is assigned to work on this feature. Example: '0','1', '2' etc.",
    )

    QA: int = Field(
        ...,
        description="Number of QA engineer is assigned to test this feature. Example: '0','1','2'.",
    )
    AI_Engineer: int = Field(
        ...,
        description="Number of AI engineer needed if there is any task related to AI. Example: '0','1','2'.",
    )


class features_list(BaseModel):
    features_list: List[feature]


def create_qa_pair_chain():
    model = ChatOpenAI(temperature=0, model="gpt-4o-mini")

    parser = PydanticOutputParser(pydantic_object=QAPair)
    prompt = PromptTemplate(
        template=qa_pair_template,
        input_variables=["requirement_document", "user_queries"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    return prompt | model | parser


qa_pair_generator_chain = create_qa_pair_chain()


def create_phase_extractor_chain():
    model = ChatOpenAI(temperature=0, model="gpt-4o-mini")

    parser = PydanticOutputParser(pydantic_object=phase_list)
    prompt = PromptTemplate(
        template=phase_template,
        input_variables=["requirement_document", "user_queries"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    return prompt | model | parser


phase_extractor_chain = create_phase_extractor_chain()


def create_feature_extractor_chain():
    model = ChatOpenAI(temperature=0, model="gpt-4o-mini")

    parser = PydanticOutputParser(pydantic_object=features_list)
    prompt = PromptTemplate(
        template=feature_template,
        input_variables=["est_sheet", "feedback", "user_queries"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    return prompt | model | parser


feature_extractor_chain = create_feature_extractor_chain()
