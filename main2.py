from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage

llm = Ollama(model="llama2")
chat_model = ChatOllama()

text = "What would be a good company name for a company that makes colorful socks?"
messages = [HumanMessage(content=text)]

v = chat_model.invoke(messages)
print(v)
# >> AIMessage(content="Socks O'Color")