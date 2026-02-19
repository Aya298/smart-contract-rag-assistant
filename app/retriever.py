from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vectorstore(splits):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        documents=splits,
        embedding=embeddings
    )

    return vectorstore


def get_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )


