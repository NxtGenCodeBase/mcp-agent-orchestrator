from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent


async def run_agent(user_query, tools):
    model = ChatOllama(model="llama3.1", temperature=0)
    agent = create_react_agent(model, tools)
    inputs = {"messages": [("user", user_query)]}
    result = await agent.ainvoke(inputs)
    return result["messages"][-1].content
