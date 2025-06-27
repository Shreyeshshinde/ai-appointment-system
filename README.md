# 🏥 AI-Powered Appointment Booking System

An intelligent system that helps users book medical appointments by analyzing symptoms using a language model (LLM), recommending departments, and scheduling appointments with available doctors. Built with **FastAPI**, **LangChain**, **HuggingFace Transformers**, and a **React + Next.js frontend**.

---

## ✨ Features

- ✅ Symptom-based department recommendation (using local LLM embeddings)
- ✅ Appointment booking with available doctors
- ✅ Department and doctor management (pre-seeded)
- ✅ Integrated React-based frontend
- ✅ CORS-enabled API
- ✅ Modular & scalable folder structure

---

## 🛠 Tech Stack

| Component     | Tech Used                      |
|---------------|-------------------------------|
| Backend       | Python, FastAPI, SQLAlchemy   |
| Embeddings    | Sentence-Transformers (local MiniLM) |
| Vector Store  | FAISS                         |
| LLM API       | HuggingFaceEndpoint via LangChain |
| Frontend      | Next.js (React)               |
| UI Framework  | ShadCN + TailwindCSS          |
| Deployment    | GitHub + Localhost (Dev)      |

---

## 🚀 Getting Started

### 🔧 Backend Setup

```bash
# Navigate to backend root
cd ai-appointment-system

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
