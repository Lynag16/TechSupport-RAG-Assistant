# main.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from operator import itemgetter
from retriever import retriever
from dotenv import load_dotenv
import os

# --- CONFIG ---
load_dotenv()  # load GEMINI_API_KEY
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- MODEL ---
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.1, 
    api_key=GEMINI_API_KEY
)

# --- Helper function ---
format_docs_runnable = RunnableLambda(lambda docs: "\n\n".join(doc.page_content for doc in docs))

# --- Prompt ---
prompt_template = """
You are a **Technical Support Assistant**. 
Use only the information from the CONTEXT below to answer the question.

If the answer isn't in the context, reply:
"I apologize, but I could not find the answer in the available user guides."

CONTEXT:
---
{context}
---

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(prompt_template)

# --- RAG chain ---
rag_chain = (
    RunnableParallel(
        context=itemgetter("question") | retriever | format_docs_runnable,
        question=RunnablePassthrough(),
    )
    | prompt
    | model
)

# --- CLI loop ---
print("💬 Knowledge Base Assistant (HuggingFace embeddings + Gemini)")
while True:
    print("\n-------------------------------")
    question = input("Ask your question (or 'q' to quit): ")
    if question.lower() == "q":
        break
    result = rag_chain.invoke({"question": question})
    print("\n🧠 Answer:\n")
    print(result.content)
