#!usr/bin/env python3

from dotenv import load_dotenv
load_dotenv()

# pip3 install langchain-community
# pip3 install beautifulsoup4
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser

async_browser = create_async_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser = async_browser)
tools = toolkit.get_tools()
print(tools)

from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatAnthropic, ChatOpenAI

# LLM不稳定，对于这个任务，可能需要跑几次才能得到正确结果
llm = ChatOpenAI(temperature = 0.5)
agent_chain = initialize_agent(
	tools,
	llm,
	agent = AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
	verbose = True)

async def main():
	response = await agent_chain.arun("What are the headers on python.langchain.com?")
	print(response)
	# 报错：openai.error.APIConnectionError: Error communicating with OpenAI

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# python3.7开始引入asyncio.run方法，可以直接替代上面两行
# asyncio.run(main())

# 协程是一种轻量级的线程，也被称为用户级线程。它是一种并发编程的方式，可以在一个线程内实现多个协作的任务，通过协程的切换来实现任务的并发执行。
# 在Python中，可以使用async和await关键字来定义和切换协程