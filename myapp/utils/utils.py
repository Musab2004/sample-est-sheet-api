import os
import tempfile


from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)
from .chains import fix_array_chain
import mimetypes
from .util_var import questions
from supabase import create_client, Client
from django.conf import settings

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

type_to_loaders = {
    ".pdf": PyPDFLoader,
    ".docx": UnstructuredWordDocumentLoader,
    ".doc": UnstructuredWordDocumentLoader,
    ".txt": TextLoader,
    ".pptx": UnstructuredPowerPointLoader,
}


class CustomFileLoader:
    loaders = type_to_loaders

    def __init__(self, file):
        self.file = file
        self.file_name = self.file.name
        self.tmp_file_name = file.url.lstrip("/")

    def load(self) -> str:
        _, file_extension = os.path.splitext(self.file_name)
        loader_class = self.loaders.get(file_extension)
        if loader_class is not None:
            print("BAse path : ", settings.BASE_DIR)
            absolute_path = os.path.join(settings.BASE_DIR, self.tmp_file_name)
            print(absolute_path)
            loader = loader_class(absolute_path)
            docs = loader.load()
            return "\n".join(doc.page_content.replace("\n", " ") for doc in docs)

    def file_url(self):
        return self.tmp_file_name

    def clean(self):
        os.remove(self.tmp_file_name)


def loading_files(uploaded_files):
    files_content = ""
    file_loaders = []
    file_names = []
    for uploaded_file in uploaded_files:
        file_loader = CustomFileLoader(uploaded_file)
        file_loaders.append(file_loader)

    for file_loader in file_loaders:
        print("loading files .......")
        files_content = files_content + "Doc Name: " + file_loader.file_name + "\n\n"
        files_content = files_content + file_loader.load() + "\n\n"
        file_names.append(file_loader.file_name)
        print(file_loader.file_url())
        upload_files(file_loader.file_name, file_loader.file_url())
    for file_loader in file_loaders:
        file_loader.clean()
    return files_content, file_names


def answer_conversion(answers):
    new_answers = []
    for ans in answers:
        if ans == "Not found in the provided document.":
            ans = ""
        new_answers.append(ans)
    return new_answers


def upload_files(file_name, file_path):
    print("file upload called")
    try:
        mime_type, _ = mimetypes.guess_type(file_path)
        mime_type = mime_type or "application/octet-stream"
        response = supabase.storage.from_("sample_est_file_storage").upload(
            file_name, file_path, {"content-type": mime_type}
        )
        print(response)
    except:
        print("exception in supabase upload")
        pass


def add_row(table, all_answers, file_name, rating, feedback):
    file_names = f"{file_name}"
    data = {
        "file_names": file_names,
        "output_df": table,
        "input_context": all_answers,
        "LLM": "gpt-4o-mini",
        "rating": rating,
        "feedback": feedback,
    }
    try:
        response = supabase.table("PromptTable").insert(data).execute()
        return response
    except Exception as e:
        print(e)


def human_readable_form(arr):
    result = ""
    if arr == None:
        return None
    for i, answer in enumerate(arr, start=1):
        result += f"{i}. {answer}\n\n"
    return result


def process_stream(inputs, config, app):

    for output in app.stream(inputs, config):
        for key, value in output.items():
            if key == "qa_pair_generator_feature":
                table = None
                answers = value["qa_pair"]
            if key == "feature_extractor":
                table = value["estimation_table"]
                answers = None
                return table, answers
    return table, answers
