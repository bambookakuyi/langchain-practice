#!usr/bin/env python3

# 要点：
# ReAct框架是指Reasoning(推理)和Acting(行动)
# LangChain中”代理“和”链“的差异：
#   在链中，一系列操作被硬编码（代码中）。
#   在代理中，语言模型被用作推理引擎来确定要采取哪些操作以及按什么顺序执行这些操作。

# 1. 为大模型提供Google搜索工具
# https://serpapi.com 注册账号，拿到SERPAPI_API_KEY

# 2.安装SerpAPI包 和 LLMMathChain 需要的 numexpr 包
# pip3 install google-search-results
# pip3 install numexpr

from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv
load_dotenv()

import langchain
langchain.debug = True

llm = OpenAI(temperature = 0)
tools = load_tools(["serpapi", "llm-math"], llm = llm)
agent = initialize_agent(tools, llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)
# breakpoint()
agent.run("目前市场上玫瑰花的平均价格是多少？如果我在此基础上加价15%卖出，应该如何定价？")
# 上面推理过程和结果都是英文的，提示用中文回复就一直报错：raised error: 'average_price_of_roses'. Please try again with a valid numerical expression
# agent.run("目前中国市场上玫瑰花的平均价格是多少人民币？如果我在此基础上加价15%卖出，应该如何定价？结果用中文回复")
