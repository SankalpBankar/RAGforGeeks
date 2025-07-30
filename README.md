# 📚RAGforGeeks 🤖🔍 👓
A powerful Retrieval-Augmented Generation (RAG) assistant designed to provide accurate and contextual answers from GeeksforGeeks Nation SkillUp content.

📁 Project Directory Structure 🧠💬
RAGforGeeks-ChatBot/

├── backend/
│   ├── models/                   # Store downloaded LLM (e.g., LLaMA2) 🧠
│   ├── vectorstores/            # Vector DB for storing embeddings 📦
│   │   └── db_faiss/            # FAISS index files 📁
│   ├── model.py                 # LLM + retrieval logic using LangChain 🛠️
│   ├── initialize_faiss.py      # FAISS setup script ⚙️
│
├── frontend/
│   └── app.py                   # Streamlit UI for chatbot 💻
│
├── setup.txt                    # LLM model setup instructions 📝
├── requirements.txt             # Python dependencies 📦
├── README.md                    # Project overview 📘




💡 Tech Stack 🛠️
•	Python 🐍 (Core programming language for backend logic)
•	Llama 2 (GGML) 🦙 (Large Language Model used for answering queries locally)
•	LangChain 🔗 (Framework for implementing RAG — Retrieval Augmented Generation)
•	FAISS 🔍 (For storing and searching vector embeddings efficiently)
•	ChromaDB 🗂️ (Optional vector store library used by LangChain)
•	CTransformers ⚡ (Lightweight LLM inference for GGML models)
•	Streamlit 🌐 (Frontend UI framework to interact with the chatbot)
•	Groq API 🚀 (For high-speed LLM inference using GroqCloud)
•	dotenv 🔐 (To manage API keys securely via environment variables)


⚙️ Setup & Installation for RAGforGeeks 🧠💬
Follow these steps to set up and run your RAG-based chatbot:

1️⃣ Clone the Repository 📥
git clone https://github.com/SankalpBankar/RAGforGeeks.git
cd RAGforGeeks

2️⃣ Install Dependencies 📦
Ensure you're using Python 3.9+, then install all required libraries:
pip install langchain groq chromadb tiktoken langchain-groq langchain-community pymupdf

3️⃣ Configure Environment 🔐
Set your GROQ API key securely using an environment variable:
import os
os.environ["GROQ_API_KEY"] = "your-groq-api-key"
(Or use .env with python-dotenv if running locally.)

4️⃣ Load the LLM (LLaMA3) 🦙
The code uses LangChain + Groq to load the model:
from langchain_groq import ChatGroq
llm = ChatGroq(
    groq_api_key=os.environ["GROQ_API_KEY"],
    model_name="llama3-8b-8192"
)
5️⃣ Run Your Application 🚀
Ensure you have all backend files and Streamlit app ready. Then run:
streamlit run app.py

🛠️ Troubleshooting 🚨
•	API Key Error
Set your key using: 
os.environ["GROQ_API_KEY"] = "your-api-key"

•	FAISS Index Empty or Missing
Run the initialize_faiss.py script to embed and store documents.






