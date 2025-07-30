# 📚RAGforGeeks 🤖🔍 👓
A powerful Retrieval-Augmented Generation (RAG) assistant designed to provide accurate and contextual answers from GeeksforGeeks Nation SkillUp content.


## 📁 Project Directory Structure 🧠💬

```
RAGforGeeks-ChatBot/
│── backend/
│   │── models/                         # Stores the Llama 2 model (download separately) 🧠
│   │── vectorstores/                    # Stores FAISS database 🗄️
│   │   └── db_faiss/                     # FAISS index files 📁
│   │── model.py                         # Main backend logic (LLM, FAISS retrieval) 🔧
│   └── initialize_faiss.py              # Script to initialize FAISS (if needed) ⚙️
│
│── frontend/
│   │── app.py                           # Streamlit web interface for chatbot 🖥️
│
│── setup.txt                            # Instructions to download the Llama 2 model 📝
│── requirements.txt                      # Dependencies for the project 📦
│── README.md                            # Project documentation 📚
```


## 💡 Tech Stack 🛠️
•	Python 🐍 (Core programming language for backend logic)\n
•	Llama 2 (GGML) 🦙 (Large Language Model used for answering queries locally)\n
•	LangChain 🔗 (Framework for implementing RAG — Retrieval Augmented Generation)\n
•	FAISS 🔍 (For storing and searching vector embeddings efficiently)\n
•	ChromaDB 🗂️ (Optional vector store library used by LangChain)\n
•	CTransformers ⚡ (Lightweight LLM inference for GGML models)\n
•	Streamlit 🌐 (Frontend UI framework to interact with the chatbot)\n
•	Groq API 🚀 (For high-speed LLM inference using GroqCloud)\n
•	dotenv 🔐 (To manage API keys securely via environment variables)\n


## ⚙️ Setup & Installation for RAGforGeeks 🧠💬\n
Follow these steps to set up and run your RAG-based chatbot:\n
1️⃣ Clone the Repository 📥\n
git clone https://github.com/SankalpBankar/RAGforGeeks.git\n
cd RAGforGeeks\n

2️⃣ Install Dependencies 📦\n
Ensure you're using Python 3.9+, then install all required libraries:\n
pip install langchain groq chromadb tiktoken langchain-groq langchain-community pymupdf\n

3️⃣ Configure Environment 🔐\n
Set your GROQ API key securely using an environment variable:\n
import os\n
os.environ["GROQ_API_KEY"] = "your-groq-api-key"
(Or use .env with python-dotenv if running locally.)\n

4️⃣ Load the LLM (LLaMA3) 🦙\n
The code uses LangChain + Groq to load the model:\n
from langchain_groq import ChatGroq\n
llm = ChatGroq(\n
    groq_api_key=os.environ["GROQ_API_KEY"],\n
    model_name="llama3-8b-8192"\n
)

5️⃣ Run Your Application 🚀\n
Ensure you have all backend files and Streamlit app ready. Then run:\n
streamlit run app.py\n

## 🛠️ Troubleshooting 🚨\n
•	API Key Error\n
Set your key using:\n 
os.environ["GROQ_API_KEY"] = "your-api-key"\n

•	FAISS Index Empty or Missing\n
Run the initialize_faiss.py script to embed and store documents.\n






