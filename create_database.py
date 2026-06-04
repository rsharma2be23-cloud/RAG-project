# 📄 Load PDF → ✂️ Split → 🔢 Embed → 📦 Store in Chroma (Vector DB)

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

# 🔐 Load API keys from .env file (e.g., MISTRAL_API_KEY)
load_dotenv()

# 📄 Step 1: Load PDF file and extract text as Document objects (page-wise)
data = PyPDFLoader("document_loaders/Sample.pdf")
docs = data.load()  # List of Documents

# ✂️ Step 2: Split large text into smaller chunks for better embedding
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Max characters per chunk
    chunk_overlap=200     # Overlap to preserve context between chunks
)
chunks = splitter.split_documents(docs)  # List of smaller Documents

# 🔢 Step 3: Initialize embedding model (converts text → vectors)
embedding_model = MistralAIEmbeddings(model="mistral-embed")

# 📦 Step 4: Store chunks + embeddings in Chroma vector database
vectorstore = Chroma.from_documents(
    documents=chunks,         # Text chunks
    embedding=embedding_model, # Embedding function
    persist_directory="chroma_db"  # Folder to save DB locally
)

# ✅ Result:
# Your PDF is now converted into a searchable vector database.
