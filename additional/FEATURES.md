# Features

## Retrieval-Augmented Generation (RAG)

This project uses Retrieval-Augmented Generation to provide context-aware answers from stored documents.

## Vector Database

- ChromaDB is used for vector storage.
- Embeddings are persisted locally.

## Embedding Model

- HuggingFace BGE Small Embeddings
- Converts text into vector representations.

## Retrieval Methods

### Similarity Search
Retrieves the most relevant document chunks.

### MMR Retrieval
Balances relevance and diversity in retrieved results.

### Multi-Query Retrieval
Generates multiple query variations to improve retrieval quality.

## Language Model

- Mistral AI
- Generates responses using retrieved context.

## Current Capabilities

- Document loading
- Embedding generation
- Vector storage
- Context retrieval
- Question answering