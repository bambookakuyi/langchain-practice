#!/usr/bin/env python3

from dotenv import load_dotenv
load_dotenv()

from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

llm = OpenAI(temperature = 0)
search = SerpAPIWrapper()
tools = [
  Tool(
  	name = "Intermediate Answer",
  	func = search.run,
  	description = "useful for when you need to ask with search"
  )
]
self_ask_with_search = initialize_agent(
	tools, llm, agent = AgentType.SELF_ASK_WITH_SEARCH, verbose = True) #, handle_parsing_errors=True)
# 查看与 ZERO_SHOT_REACT_DESCRIPTION 的区别
# self_ask_with_search = initialize_agent(
# 	tools, llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)
self_ask_with_search.run("使用农历的国家首都是哪里？")
# 报错：langchain_core.exceptions.OutputParserException: Could not parse output:  No.
# Final answer: 中国