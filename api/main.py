from fastapi import FastAPI, UploadFile, File, APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv

from app.ingestion import load_document, split_documents
from app.retriever import create_vectorstore, get_retriever
from app.memory import get_memory
from app.chains import build_rag_chain

load_dotenv()

app = FastAPI()
router = APIRouter()

rag_chain = None


class QuestionRequest(BaseModel):
    question: str


@router.post("/upload")
async def upload_contract(file: UploadFile = File(...)):
    global rag_chain

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    docs = load_document(file_path)
    splits = split_documents(docs)
    vectorstore = create_vectorstore(splits)
    retriever = get_retriever(vectorstore)
    memory = get_memory()
    rag_chain = build_rag_chain(retriever, memory)

    return {"message": "Document processed successfully"}


@router.post("/ask")
def ask_question(request: QuestionRequest):
    global rag_chain

    if rag_chain is None:
        return {"answer": "Upload a document first."}

    result = rag_chain.invoke({"question": request.question})

    return {"answer": result["answer"]}


# Register routes
app.include_router(router)