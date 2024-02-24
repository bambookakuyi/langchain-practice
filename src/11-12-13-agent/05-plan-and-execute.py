#!usr/bin/env python3

# Plan and execute 代理
# 这种代理的独特之处在于，它的计划和执行不再是由同一个代理所完成，而是：
#   计划由一个大语言模型代理（负责推理）完成。
#   执行由另一个大语言模型代理（负责调用工具）完成。

from dotenv import load_dotenv
load_dotenv()

# pip3 install langchain langchain_experimental
from langchain.chat_models import ChatOpenAI
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain.llms import OpenAI
from langchain import SerpAPIWrapper
from langchain.agents.tools import Tool
from langchain import LLMMathChain

search = SerpAPIWrapper()
llm = OpenAI(temperature = 0)
llm_math_chain = LLMMathChain.from_llm(llm = llm, verbose = True)
tools = [
  Tool(
  	name = "Search",
  	func = search.run,
  	description = "useful for when you need to answer questions about current events"
  ),
  Tool(
  	name = "Calculator",
  	func = llm_math_chain.run,
  	description = "useful for when you need to answer questions about math"
  )
]
model = ChatOpenAI(model_name = "gpt-3.5-turbo-0125", temperature = 0)
model2 = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature = 0)
planner = load_chat_planner(model)
executor = load_agent_executor(model2, tools, verbose = True)
agent = PlanAndExecute(planner = planner, executor = executor, verbose = True)
# agent.run("在纽约，100美元可以吃什么肉或蔬菜？")
# 报错：openai.error.RateLimitError: Rate limit reached

agent.run("在纽约，100美元可以买几束玫瑰花？")
