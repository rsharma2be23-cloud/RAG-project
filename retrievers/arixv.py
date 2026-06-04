from langchain_community.retrievers import ArxivRetriever

retriever=ArxivRetriever(
  load_max_docs=3,
  load_all_available_meta=True# other info 
)

docs=retriever.invoke("transformer neural networks")# 

for i,doc in enumerate(docs):
  print(f"Summary: {doc.page_content[:200]}...")
  print(f"Published: {doc.metadata.get('Published')}")
  print(f"Authors: {doc.metadata.get('Authors')}")