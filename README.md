# 💬 TechSupport-RAG-Assistant

An intelligent **Technical Support Assistant** that answers user questions from **PDF manuals or guides** using **Retrieval-Augmented Generation (RAG)**.  

This assistant combines **Hugging Face embeddings** (for semantic document search) with **Google Gemini** (for natural-language generation), providing **accurate, step-by-step technical support answers** based on your own documentation.

---

## 🚀 Features

✅ **Acts like a support engineer** — gives structured, step-by-step help and explanations.  
✅ **Local embeddings** — uses `sentence-transformers/all-MiniLM-L6-v2` (no external API calls).  
✅ **Gemini-powered generation** — high-quality, context-aware answers via `gemini-2.5-flash`.  
✅ **Automatic document processing** — reads and splits PDFs automatically from `knowledge_base_docs/`.  
✅ **Persistent vector store** — stores embeddings using **Chroma** for fast retrieval.  
✅ **Terminal chat interface** — easy to use locally, without any web interface required.  

---

## 🧠 Architecture Overview

```
PDF Documents → Text Splitter → HuggingFace Embeddings → Chroma DB → Gemini → User Answer
```

---

## 🛠️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/TechSupport-RAG-Assistant.git
cd TechSupport-RAG-Assistant
```

### 2️⃣ Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in the `app/` folder with your Gemini API key:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

🔗 Get your key from: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## 📂 Project Structure

```
TechSupport-RAG-Assistant/
│
├── app/
│   ├── main.py                # CLI chatbot app (Gemini-powered)
│   ├── retriever.py           # Document loader, splitter, embeddings, and Chroma setup
│   ├── .env                   # Gemini API key
│
├── requirements.txt
│
├── knowledge_base_docs/       # PDF manuals & user guides
│
└── chroma_langchain_db/       # Auto-generated Chroma vector database
```

---

## ▶️ Usage

Run the assistant locally:

```bash
cd app
python3 main.py
```

Then ask questions directly in your terminal 👇

```
📚 Technical Support Assistant
-------------------------------
Ask your question (or 'q' to quit): How do I reset my device?

🧠 Answer:
1. Go to “Settings.”
2. Select “System.”
3. Choose “Reset Options.”
4. Confirm to restore factory settings.
```

---

## ⚙️ Technologies Used

| Component | Technology |
|------------|-------------|
| **LLM** | Google Gemini (`gemini-2.5-flash`) |
| **Embeddings** | Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`) |
| **Vector Store** | Chroma |
| **Framework** | LangChain |
| **PDF Loader** | PyPDF |
| **Environment** | python-dotenv |

---

## 💡 Example Use Cases

- Internal **technical documentation chatbot**  
- Automated **IT support assistant**  
- Intelligent **FAQ engine**  
- Smart **manual search tool**

---

## 🧾 License

MIT License © 2025 
