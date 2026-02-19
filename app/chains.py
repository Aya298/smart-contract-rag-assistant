from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain


def build_rag_chain(retriever, memory):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0.2,
        convert_system_message_to_human=True  
        
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )
