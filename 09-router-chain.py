#!usr/bin/env python3

# 要点：RouterChain，也叫路由链，会根据输入确定适合的处理模板，如果没有找到合适的，则发送到默认链

# 1. 构建两个场景的模板
flower_care_template = """你是一个经验丰富的园丁，擅长解答关于养花育花的问题。
                        下面是需要你来回答的问题:
                        {input}"""

flower_deco_template = """你是一位网红插花大师，擅长解答关于鲜花装饰的问题。
                        下面是需要你来回答的问题:
                        {input}"""

# 构建提示信息
prompt_infos = [
    {
        "key": "flower_care",
        "description": "适合回答关于鲜花护理的问题",
        "template": flower_care_template,
    },
    {
        "key": "flower_decoration",
        "description": "适合回答关于鲜花装饰的问题",
        "template": flower_deco_template,
    }]

# 2. 初始化语言模型
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
llm = OpenAI(model = "gpt-3.5-turbo-instruct", temperature = 0.7)

# 3. 构建目标链
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
chain_map = {}
for info in prompt_infos:
	prompt = PromptTemplate(template = info["template"], input_variables = ["input"])
	print("目标提示\n", prompt)
	chain = LLMChain(llm = llm, prompt = prompt, verbose = True)
	chain_map[info["key"]] = chain

# 4. 构建路由链
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE as RouterTemplate
descriptions = [f"{p['key']}: {p['description']}" for p in prompt_infos]
router_template = RouterTemplate.format(destinations = "\n".join(descriptions))
print("路由模版:\n", router_template)
router_prompt = PromptTemplate(
	template = router_template,
	input_variables = ["input"],
	output_parser = RouterOutputParser())
print("路由提示:\n", router_template)
router_chain = LLMRouterChain.from_llm(llm, router_prompt, verbose = True)

# 5. 构建默认链
from langchain.chains import ConversationChain
default_chain = ConversationChain(llm = llm, output_key = "text", verbose = True)

# 6. 使用MultiPromptChain多路由链将几个链整合在一起
from langchain.chains.router import MultiPromptChain
chain = MultiPromptChain(
	router_chain = router_chain,
	destination_chains = chain_map,
	default_chain = default_chain,
	verbose = True)

# 7. 运行路由链
# 测试A:
# print(chain.run("如何为康乃馨浇水？"))

# # 测试B:
# print(chain.run("如何为年会场地装饰花朵？"))

# 测试 default_chain
print(chain.run("程序员怎么做职业规划？"))

# # 因为RouterChain返回结果不稳定，测试 default_chain 时，一致报错: raise OutputParserException(langchain_core.exceptions.OutputParserException: Parsing text...
# # 解决方法：使用第7节课的OutputFixingParser来修复看看
# # 这个方法不行，因为是在中间调用RouterChain的时候，返回结果格式不正确，而MultiPromptChain包含多个Chain，即包含多个结果格式，不能用同个parser处理
# # 目前只能重试chain.run
# from langchain.output_parsers import PydanticOutputParser
# from pydantic import BaseModel, Field
# class DestinationTemplate(BaseModel):
# 	description: str = Field(description = "name of template")
# 	next_inputs: str = Field(description = "input string")
# parser = PydanticOutputParser(pydantic_object = DestinationTemplate)

# from langchain.output_parsers import OutputFixingParser
# output_fixing_parser = OutputFixingParser.from_llm(parser = parser, llm = llm)
# output_fixing_parser.parse(chain.run("程序员怎么做职业规划？"))
























