from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

loader = TextLoader("knowledge_base/hospital_knowledge.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # FREE
db = FAISS.from_documents(docs, embedding)
db.save_local("vector_store")

print("✅ Vector store created with HuggingFace embeddings!")
