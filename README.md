# Email RAG System

A Retrieval-Augmented Generation (RAG) system that reads Gmail emails, stores them as embeddings, and answers user questions using an LLM.

# What it does
Fetches emails from Gmail (IMAP)
Stores email text locally
Uses FAISS for semantic search
Retrieves relevant emails based on query
Generates answers using google/flan-t5-large

# Tech Stack
Python
FAISS (vector search)
Sentence Transformers (embeddings)
Gmail IMAP
Hugging Face / Flan-T5 LLM

# Workflow
Gmail → Email Extraction → Embeddings → FAISS → Query → LLM → Answer

# How to run
python ingest.py   
python query.py 

# Requirements
Gmail App Password (for IMAP)
Python dependencies from requirements.txt

# Output Example
Security alert emails detected
Meetings scheduled at specific times
Summaries of inbox content
🏁 Goal

Enable natural language Q&A over your Gmail inbox using a simple RAG pipeline.
