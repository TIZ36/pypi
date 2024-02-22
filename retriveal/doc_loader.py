from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader

loader = TextLoader("test.md")
v= loader.load()
print(v)

loader = DirectoryLoader('./docs/', glob='**/*')
docs = loader.load()

print(docs)