#!/usr/bin/env python3

from dotenv import load_dotenv
load_dotenv()

from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.utils import build_resource_service, get_gmail_credentials

# toolkit = GmailToolkit()
credentials = get_gmail_credentials(
	token_file="token.json",
	scopes=["https://mail.google.com/"],
	client_secrets_file="credentials.json"
)
api_reesource = build_resource_service(credentials = credentials)
toolkit = GmailToolkit(api_reesource = api_reesource)

tools = toolkit.get_tools()
print(tools)

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

llm = ChatOpenAI(temperature = 0)#, model = "gpt-4")
agent = initialize_agent(
	tools = tools,
	llm = llm,
	agent = AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
	verbose = True
)
result = agent.run("今天TC给我发邮件了吗？最新的邮件是谁发给我的？")
