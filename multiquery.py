from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_mistralai import ChatMistralAI
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Sample documents
docs = [
    Document(page_content="Artificial intelligence is transforming industries by automating tasks and enabling data-driven decision making."),
    Document(page_content="Machine learning is a subset of AI that allows systems to learn patterns from data without explicit programming."),
    Document(page_content="Deep learning uses neural networks with multiple layers to solve complex problems such as image recognition and natural language processing."),
    Document(page_content="Retrieval-Augmented Generation combines information retrieval with large language models to provide more accurate and up-to-date responses."),
    Document(page_content="Vector databases store embeddings and enable efficient similarity search for semantic retrieval applications.")
]

# Embedding model
embedding_model = MistralAIEmbeddings(
    model="mistral-embed"
)

# LLM used to generate multiple query variations
llm = ChatMistralAI(
    model="mistral-large-latest"
)

# Create vector store
vectorstore = Chroma.from_documents(
    docs,
    embedding_model
)

# Basic retriever
retriever = vectorstore.as_retriever()

# Multi-query retriever
multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm
)

query = "What is Retrieval-Augmented Generation?"

retrieved_docs = multi_query_retriever.invoke(query)

print("\nRetrieved Documents:\n")

for doc in retrieved_docs:
    print(doc.page_content)
    print("-" * 50)