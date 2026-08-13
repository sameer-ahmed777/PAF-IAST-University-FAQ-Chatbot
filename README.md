# 🎓 PAF-IAST University FAQ Chatbot

An AI-powered University FAQ Chatbot developed using Retrieval-Augmented Generation (RAG), FAISS Vector Search, and Streamlit.

---

## 📌 Project Overview

The PAF-IAST University FAQ Chatbot is designed to help students quickly access information related to:

- Attendance Policies
- Admission Requirements
- Examination Rules
- Scholarship Information
- Library Regulations
- Hostel Rules
- Academic Guidelines

The system processes university documents and provides context-based answers through an interactive web interface.

---

## 🚀 Key Features

✅ PDF Document Processing

✅ Text Extraction

✅ Text Chunking

✅ Knowledge Retrieval

✅ FAISS Vector Database

✅ Streamlit Web Interface

✅ Student Query Support

✅ University FAQ Assistance

---

## 🏗️ System Architecture

```text
University Documents (PDFs)
            │
            ▼
      Text Extraction
            │
            ▼
        Chunking
            │
            ▼
       Embeddings
            │
            ▼
    FAISS Vector Store
            │
            ▼
       Retrieval
            │
            ▼
      RAG Pipeline
            │
            ▼
      Streamlit UI
            │
            ▼
      Student Answer
```

---

## 📂 Project Structure

```text
RAG-UNIVERSITY-CHATBOT
│
├── app
│   └── app.py
│
├── data
│   ├── raw
│   └── processed
│
├── src
│   ├── ingest.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── faiss_manager.py
│   ├── search_engine.py
│   ├── chatbot.py
│   └── rag_pipeline.py
│
├── tests
├── screenshots
├── vector_store
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Frontend
- Streamlit

### Backend
- Python

### Libraries
- NumPy
- PyPDF
- FAISS

### AI Components
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Database

---

## ⚙️ Installation

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
py -m streamlit run app/app.py
```

Open the application in your browser:

```text
http://localhost:8501
```

---

## 💬 Sample Questions

```text
What is the attendance policy?

What are the admission requirements?

What are the scholarship requirements?

What are the hostel regulations?

What are the library rules?

What are the examination rules?
```

---

## 📸 Screenshots

Store project screenshots inside:

```text
screenshots/
```

Example:

```text
home_page.png
attendance_query.png
hostel_query.png
scholarship_query.png
```

---

## 🔮 Future Enhancements

- Gemini AI Integration
- Multi-PDF Knowledge Base
- Chat History
- Voice Assistant Support
- Advanced Semantic Search
- Source Citation System

---

## 👨‍💻 Developer

**Sameer Ahmed**

PAF-IAST AI Project

University FAQ Chatbot System

---

## 📜 License

MIT License

Copyright © 2026 Sameer Ahmed

All Rights Reserved.
