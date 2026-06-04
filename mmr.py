from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

# Sample documents to store in vector DB
docs = [
    Document(page_content="Artificial intelligence is transforming industries by automating tasks and enabling data-driven decision making."),
    
    Document(page_content="Machine learning is a subset of AI that allows systems to learn patterns from data without explicit programming."),
    
    Document(page_content="Deep learning uses neural networks with multiple layers to solve complex problems such as image recognition and natural language processing."),
    
    Document(page_content="Retrieval-Augmented Generation combines information retrieval with large language models to provide more accurate and up-to-date responses."),
    
    Document(page_content="Vector databases store embeddings and enable efficient similarity search for semantic retrieval applications.")
]

# Convert text into embeddings (vectors)
embeddings = HuggingFaceBgeEmbeddings(
  model_name=="BAAI/bge-small-en-v1.5"
)

# Create vector store and save document embeddings
vectorstore = Chroma.from_documents(docs, embeddings)

# Create retriever for similarity search
similarity_retriever = vectorstore.as_retriever(
    search_type="similarity",      # Search by vector similarity
    search_kwargs={"k": 3}         # Return top 3 matches
)

# Search query
query = "What is RAG?"

# Retrieve most relevant documents
retrieved_docs = similarity_retriever.invoke(query)

print("Results of Similarity Search:\n")

# Display retrieved documents
for i, doc in enumerate(retrieved_docs, start=1):
    print(f"Result {i}:")
    print(doc.page_content)
    print()