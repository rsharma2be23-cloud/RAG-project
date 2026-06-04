from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
#from langchain_community.document_loaders import TextLoader
#from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma

from langchain_core.prompts import ChatPromptTemplate
#from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

load_dotenv()



model = ChatMistralAI(model="mistral-small-2506")

embedding_model = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vectorStore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vectorStore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)

llm = ChatMistralAI(model="mistral-small-2506")
template = ChatPromptTemplate.from_messages(
    [
        ("system", """You are an helpful ai assistant
        use only the provided context to answet the question
        
        if answer not present in the context say " i could not find the answer in the given documents" """),
        ("human", """Context:
        {context}

        Question:
        {question}
        """       )
    ]
)

print("Rag system created")
print("press 0 to exit")

while True:
  query=input("You: ")
  if query=="0":
    break

  docs = retriever.invoke(query)

  context = "\n\n".join(
      [doc.page_content for doc in docs]
  )

  final_prompt = template.invoke({
      "context": context,
      "question": query
  })

  response = llm.invoke(final_prompt)

  print(f"\nAI: {response.content}\n")