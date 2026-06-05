# Known Issues and Limitations

## Current Limitations

### Local Vector Database
The project currently uses a local ChromaDB instance and is not configured for cloud deployment.

### Limited Document Formats
Support for document formats is currently limited and may require additional loaders.

### No Conversation Memory
The system processes each query independently and does not maintain chat history.

### No Source Citations
Retrieved document sources are not displayed in the final response.

### Environment Configuration
Users must manually configure API keys through a `.env` file.

### Scalability
Performance may decrease when working with very large document collections.

## Planned Improvements

- Add conversational memory
- Add source attribution
- Support more document formats
- Add web-based interface
- Improve retrieval accuracy
- Enable cloud deployment