from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline

# Load vector store
embedding = HuggingFaceEmbeddings(model_name="local_model")
db = FAISS.load_local("vector_store", embedding, allow_dangerous_deserialization=True)

# Load local Flan-T5 model
model_name = "google/flan-t5-base"  # Already available locally if downloaded
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_length=256)
llm = HuggingFacePipeline(pipeline=pipe)

# Define Prompt
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Use the following context to answer the question at the end. If unsure, say "No department found".

{context}

Question: {question}
""",
)

# Define LangChain chain
qa_chain = LLMChain(llm=llm, prompt=prompt_template)

def analyze_symptoms(symptom_text: str) -> str:
    print("🩺 Received symptom input:", symptom_text)

    try:
        docs = db.similarity_search(symptom_text, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        question = f"""You are a medical assistant.
Based on the given symptoms, return only the department name most likely to handle the case.

Departments:
Cardiology, Neurology, Dermatology, Pulmonology, Orthopedics, General Medicine

Symptoms:
{symptom_text}

Instructions:
Return EXACTLY one department name from the list above. If no department matches, return "No department found"."""

        result = qa_chain.invoke({"context": context, "question": question})
        print("🧠 Specialty returned:", result["text"].strip())
        return result["text"].strip()

    except Exception as e:
        print("❌ Error in analyze_symptoms:", e)
        return "No department found"
