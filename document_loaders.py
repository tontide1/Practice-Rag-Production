import os
import tempfile
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, WebBaseLoader, DirectoryLoader, PyPDFLoader, UnstructuredWordDocumentLoader, UnstructuredPowerPointLoader, UnstructuredMarkdownLoader

load_dotenv()


# tạo 1 hàm load text
def load_text_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"Hello, this is a sample text file.")
        temp_file_path = temp_file.name

    try:
        loader = TextLoader(temp_file_path)
        documents = loader.load()

        for doc in documents:
            print(doc)
            print("-----------------------------------------")

            print(doc.page_content)

    finally:
        os.remove(temp_file_path)

def pdf_loader(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} documents from PDF.")
    for i, doc in enumerate(documents):
        print(i, doc.page_content)
        print(doc.metadata)
    
if __name__ == "__main__":
    # load_text_file()
    path_pdf = "docs/langchain_demo.pdf"
    pdf_loader(path_pdf)