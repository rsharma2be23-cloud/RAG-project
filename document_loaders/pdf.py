from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data=PyPDFLoader("document_loaders/Sample.pdf")

docs=data.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=5
)
chunks=splitter.split_documents(docs)
print(len(docs))