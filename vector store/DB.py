from langchain_community.vectorstores import Chroma

from langchain_mistralai import MistralAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

from langchain_core.documents import Document

docs =[
  Document(page_content="Octopuses have three hearts—two pump blood to the gills, and one pumps it to the rest of the body",metadata={"source":"AI_book"}),

    Document(page_content="Even stranger, their blood is blue because it uses copper-based hemocyanin instead of iron-based hemoglobin.",metadata={"source":"my_book"}),

      Document(page_content="The Anglo-Zanzibar War between Britain and Zanzibar in 1896 lasted about 38–45 minutes. Zanzibar surrendered almost immediately after British bombardment began.",metadata={"source":"your_book"})
]


embedding_model = MistralAIEmbeddings(
    model="mistral-embed",
)

vectorstore= Chroma.from_documents(
  documents=docs,
  embedding=embedding_model,
  persist_directory="chroma-db"
)
#Chroma compares it with stored embeddings
#Finds the most similar meanings, not exact words

result=vectorstore.similarity_search("how many hearts octopuses have",k=2)# give 2 most similar documents to this

for r in result:
  print(r)

retriever=vectorstore.as_retriever()
docs=retriever.invoke("Explain octopuses")

for d in docs:
  print(d.page_content)