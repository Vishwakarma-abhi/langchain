# 🚀 RAG Chatbot using Groq + LangChain + Ollama + FAISS + Streamlit

A simple **Retrieval-Augmented Generation (RAG)** application built using **Groq's ultra-fast inference**, **LangChain**, **Ollama Embeddings**, **FAISS Vector Store**, and **Streamlit**.

The application loads documentation from a website, converts it into vector embeddings using an open-source embedding model running locally via Ollama, retrieves the most relevant chunks, and generates answers using Groq-hosted LLMs.

---

# ✨ Features

- ⚡ Ultra-fast LLM inference using **Groq**
- 📚 Website document loading
- ✂️ Intelligent text chunking
- 🧠 Local embeddings via **Ollama**
- 🔍 Semantic Search using **FAISS**
- 💬 Retrieval Augmented Generation (RAG)
- 📄 Display retrieved document chunks
- 🎈 Interactive Streamlit UI

---

# Tech Stack

| Component | Technology |
|------------|------------|
| UI | Streamlit |
| LLM | Groq |
| Framework | LangChain |
| Embeddings | Ollama |
| Embedding Model | nomic-embed-text |
| Vector Database | FAISS |
| Loader | WebBaseLoader |
| Text Splitter | RecursiveCharacterTextSplitter |
| Prompt Engineering | LangChain Prompt Templates |

---

# Project Architecture

```
                     User Query
                         │
                         ▼
                Streamlit Web App
                         │
                         ▼
                Retrieval Chain
                         │
             ┌───────────┴────────────┐
             │                        │
             ▼                        ▼
      FAISS Retriever          ChatGroq LLM
             ▲                        ▲
             │                        │
      Vector Embeddings        Prompt Template
             ▲
             │
    Ollama Embedding Model
      (nomic-embed-text)
             ▲
             │
      Document Chunks
             ▲
             │
RecursiveCharacterTextSplitter
             ▲
             │
       WebBaseLoader
             ▲
             │
https://docs.smith.langchain.com/
```

---

# Complete RAG Workflow

```
              Website URL
                   │
                   ▼
          WebBaseLoader
                   │
                   ▼
        Raw LangChain Documents
                   │
                   ▼
 RecursiveCharacterTextSplitter
                   │
                   ▼
         Document Chunks
                   │
                   ▼
    Ollama Embedding Model
    (nomic-embed-text)
                   │
                   ▼
          Dense Embeddings
                   │
                   ▼
         FAISS Vector Store
                   │
────────────────────────────────────────
               User asks question
────────────────────────────────────────
                   │
                   ▼
           Similarity Search
                   │
                   ▼
      Top Relevant Document Chunks
                   │
                   ▼
      Prompt + Retrieved Context
                   │
                   ▼
       Groq Hosted LLM (Llama)
                   │
                   ▼
           Final Response
```

---

# Folder Structure

```
RAG-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── assets/
```

---

# Pipeline Explanation

## Step 1

Load documentation

```python
loader = WebBaseLoader(url)
```

↓

Loads web pages as LangChain Documents.

---

## Step 2

Split documents

```python
RecursiveCharacterTextSplitter
```

↓

Breaks large documents into overlapping chunks.

```
Chunk Size = 1000
Overlap = 200
```

---

## Step 3

Generate embeddings

```python
OllamaEmbeddings(
    model="nomic-embed-text"
)
```

↓

Converts every chunk into numerical vectors locally.

---

## Step 4

Store vectors

```python
FAISS.from_documents(...)
```

↓

Creates an efficient vector index for semantic retrieval.

---

## Step 5

User asks question

```
"What is LangSmith?"
```

↓

Converted into embedding

↓

Similarity Search

↓

Top matching chunks returned.

---

## Step 6

Prompt Construction

```
Context

+
User Question

↓

LLM
```

Prompt Template:

```
<context>

Retrieved Chunks

</context>

Question:
....
```

---

## Step 7

Groq LLM

```python
ChatGroq(
model="llama-3.3-70b-versatile"
)
```

↓

Reads retrieved context

↓

Generates final answer.

---
