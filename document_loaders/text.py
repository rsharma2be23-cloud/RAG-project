from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

splitter=CharacterTextSplitter(
  separator="",# splits when  a new line is encountered
  chunk_size=170,
  chunk_overlap=1
)

data =TextLoader("document_loaders/notes.txt")
docs=data.load()
chunks=splitter.split_documents(docs)
print(chunks)