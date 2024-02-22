from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()

search_results = search.invoke("what is the weather in Shanghai, please answer in Chinese")

print (search_results)