# Setup Guide

## 1. Clone the Repository

```bash
git clone https://github.com/rsharma2be23-cloud/RAG-project.git
cd RAG-project
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Create Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_api_key_here
```

## 5. Create the Vector Database

```bash
python create_database.py
```

## 6. Run the Application

```bash
python main.py
```

## Technologies Used

- Python
- LangChain
- ChromaDB
- HuggingFace BGE Embeddings
- Mistral AI

## Project Components

- `create_database.py` - Creates embeddings and stores them in ChromaDB
- `main.py` - Main RAG pipeline
- `mmr.py` - Maximum Marginal Relevance retrieval
- `multiquery.py` - Multi-query retrieval