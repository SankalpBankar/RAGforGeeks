# Load environment variables
from dotenv import load_dotenv
import os
load_dotenv()

# Get GROQ API key from .env
groq_api_key = os.getenv("GROQ_API_KEY")
print("GROQ_API_KEY Loaded:", bool(groq_api_key))

# Load PDF using PyMuPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
pdf_path = "GFG_Nation_Skillup.pdf"
loader = PyMuPDFLoader(pdf_path)
documents = loader.load()

# Split documents into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splits = splitter.split_documents(documents)

# Use fake embeddings for testing (replace with real embeddings later)
from langchain_community.embeddings import FakeEmbeddings
from langchain.vectorstores import Chroma
vectorstore = Chroma.from_documents(documents=splits, embedding=FakeEmbeddings(size=1536))
retriever = vectorstore.as_retriever()

# Load Groq LLM (LLaMA3 8B)
from langchain_groq import ChatGroq
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-8b-8192"
)

# Build RetrievalQA chain
from langchain.chains import RetrievalQA
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)
que = input("Enter your question: ")
print(rag_chain.invoke(que)["result"])
