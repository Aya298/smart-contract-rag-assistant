import os
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
print("DEBUG KEY:", os.getenv("GOOGLE_API_KEY"))

from app.ingestion import load_document, split_documents
from app.retriever import create_vectorstore, get_retriever
from app.memory import get_memory
from app.chains import build_rag_chain
from app.summarizer import summarize_document

rag_chain = None
full_text = None


def build_pipeline(file):
    global rag_chain, full_text

    docs = load_document(file.name)
    full_text = "\n".join([doc.page_content for doc in docs])

    splits = split_documents(docs)
    vectorstore = create_vectorstore(splits)
    retriever = get_retriever(vectorstore)
    memory = get_memory()
    rag_chain = build_rag_chain(retriever, memory)

    return "Document processed successfully ✅"


def respond(message, history):
    global rag_chain

    if rag_chain is None:
        return "Upload a document first."

    result = rag_chain.invoke({"question": message})
    return result["answer"]


def summarize():
    global full_text

    if full_text is None:
        return "Upload a document first."

    return summarize_document(full_text)


with gr.Blocks() as demo:
    gr.Markdown("# Smart Contract Assistant")

    file_upload = gr.File(label="Upload Contract (PDF)")
    upload_btn = gr.Button("Process Document")
    status_output = gr.Textbox(label="Status")

    chatbot = gr.ChatInterface(fn=respond)

    summarize_btn = gr.Button("Summarize Contract")
    summary_output = gr.Textbox(label="Summary")

    upload_btn.click(build_pipeline, inputs=file_upload, outputs=status_output)
    summarize_btn.click(summarize, outputs=summary_output)

if __name__ == "__main__":
    demo.launch()