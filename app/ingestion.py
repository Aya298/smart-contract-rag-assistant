
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_document(file_path: str):
    """
    Load PDF or DOCX document
    """
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError("Unsupported file type. Only PDF and DOCX are allowed.")

    documents = loader.load()
    return documents


def split_documents(documents):
    """
    Split documents into chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    splits = text_splitter.split_documents(documents)
    return splits
