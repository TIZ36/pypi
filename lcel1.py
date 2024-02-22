from langchain.prompts.chat import ChatPromptTemplate
from langchain.core.output_parsers import StringOutputParser, CommaSeparatedListOutputParser
from langchain_community.chat_models import ChatOllama

chat_model = ChatOllama()
output_parser = StringOutputParser()

template = "Generate a list of 5 {text}. \n\n{format_instructions}"

chat_prompt = ChatPromptTemplate.from_template(template)

chat_prompt = chat_prompt.partial(format_instructions=output_parser.get_format_instructions())

chain = chat_prompt | chat_model | output_parser

v= chain.invoke({"text": "colors"})

print(v)