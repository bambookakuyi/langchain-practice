#!/usr/bin/env python3

# 使用 arXiv 工具开发科研助理
# ArXiv API Tool 提供访问学术论文和文献的工具

from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

llm = ChatOpenAI(temperature = 0.0)
tools = load_tools(
	["arxiv"] # pip3 imstall arxiv
)

agent_chain = initialize_agent(tools, llm,
	agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
	verbose = True)

agent_chain.run("介绍一下2403.04746这篇论文的创新点?")
# Final Answer: The innovative point of paper 2403.04746 is the simulated trial and error method proposed for tool-augmented LLMs to improve tool learning