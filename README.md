# Smart Contract Assistant

## Overview
An AI-powered assistant that analyzes smart contracts using RAG architecture.

## Features
- PDF Upload
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database
- Google Gemini LLM
- Conversation Memory
- Guardrails
- Confidence Score
- Contract Summarization
- FastAPI Backend
- Gradio Frontend

## Architecture
1. Document Ingestion
2. Text Splitting
3. Embedding Generation
4. Vector Storage (FAISS)
5. Retriever
6. LLM (Gemini)
7. Response Generation

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run Gradio
python ui/gradio_app.py

### Run Backend
uvicorn api.main:app --reload