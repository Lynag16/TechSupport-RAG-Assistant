# retriever.py
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader 
import os

# --- CONFIGURATION ---
DATA_DIR = "../knowledge_base_docs"
DB_DIR = "../chroma_langchain_db"

# --- 1. LOAD & SPLIT DOCUMENTS ---
if not os.path.exists(DATA_DIR):
    print(f"❌ Error: Directory '{DATA_DIR}' not found. Please add your PDFs.")
    documents = []
else:
    print(f"📄 Loading documents from {DATA_DIR}...")
    loader = DirectoryLoader(DATA_DIR, glob="**/*.pdf", loader_cls=PyPDFLoader)
    raw_docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    documents = text_splitter.split_documents(raw_docs)
    print(f"✅ Loaded and split into {len(documents)} chunks.")

# --- 2. EMBEDDINGS & VECTOR STORE ---
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create or load Chroma DB
add_documents = not os.path.exists(DB_DIR)
vector_store = Chroma(
    collection_name="knowledge_base", 
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

if add_documents and documents:
    print(f"🧠 Adding {len(documents)} documents to Chroma...")
    vector_store.add_documents(documents=documents)
    # vector_store.persist()
    print("✅ Vector store created and saved.")
elif add_documents and not documents:
    print("⚠️ No documents found, database will be empty.")
else:
    print("📚 Existing vector store loaded.")

# --- 3. RETRIEVER ---
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
