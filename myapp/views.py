from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FileUpload
from .serializers import FileUploadSerializer
import json
import ast
import os
import tempfile

from dotenv import load_dotenv
from io import BytesIO
from supabase import create_client, Client
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)
from langchain_openai import ChatOpenAI

from .utils.util_var import questions, phase_questions, project_phases
from .utils.utils import (
    CustomFileLoader,
    add_row,
    upload_files,
    human_readable_form,
    answer_conversion,
    loading_files,
    process_stream,
)
from .utils.graph_utils import app, show_table
import mimetypes
import hmac


load_dotenv()


class InputView(APIView):
    def post(self, request, *args, **kwargs):
        if "file" not in request.FILES:
            return Response(
                {"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        file = request.FILES["file"]
        serializer = FileUploadSerializer(data={"file": file})
        if serializer.is_valid():
            input = serializer.save()
            uploaded_files = []
            uploaded_files.append(input.file)
            config = {"configurable": {"thread_id": "thread-81"}}
            files_content, file_names = loading_files(uploaded_files)
            inputs = {
                "file": files_content,
                "questions": questions,
                "phase_questions": phase_questions,
                "project_phases": project_phases,
            }

            table, answers = process_stream(inputs, config, app)
            inputs = None
            table, answers = process_stream(inputs, config, app)
        return Response({"table": table}, status=status.HTTP_201_CREATED)
