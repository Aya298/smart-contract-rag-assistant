from langchain_google_genai import ChatGoogleGenerativeAI


def summarize_document(text):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0.3
    )

    prompt = f"""
Summarize this smart contract clearly in bullet points:

{text}
"""

    response = llm.invoke(prompt)
    return response.content