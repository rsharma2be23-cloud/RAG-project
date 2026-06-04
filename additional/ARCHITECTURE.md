# RAG Project Architecture

## Workflow

1. User asks a question
2. Query is converted into embeddings
3. ChromaDB searches for relevant document chunks
4. Retriever selects the most relevant context
5. Context is sent to Mistral AI
6. Mistral AI generates the final response

## Components

### Document Loader
Loads and processes source documents.

### Embedding Model
Uses HuggingFace BGE Small embeddings to convert text into vectors.

### Vector Database
ChromaDB stores document embeddings for efficient retrieval.

### Retriever
Supports:
- Similarity Search
- MMR Retrieval
- Multi-Query Retrieval

### LLM
Mistral AI generates responses using retrieved context.

## Future Enhancements

- Conversational Memory
- Source Citations
- Hybrid Search
- Agentic AI Workflows
- Streamlit UI