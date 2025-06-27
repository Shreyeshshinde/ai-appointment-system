from pydantic import BaseModel

class SymptomQuery(BaseModel):
    query: str
    patient_name: str

# backend/symptom_extractor.py
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings


def analyze_symptoms(query):
    db = FAISS.load_local("vector_store", OpenAIEmbeddings())
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=db.as_retriever())
    return qa.run(query)