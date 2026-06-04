from langchain_community.document_loaders import WebBaseLoader

url="https://www.tesla.com/"

data=WebBaseLoader(url)

docs=data.load()

print(len(docs))