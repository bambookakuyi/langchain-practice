#!usr/bin/env python3

from dotenv import load_dotenv
load_dotenv()

# 1、使用LLMChain将提示模板的构建和模型的调用封装到一起
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
template = "{flower}的花语是？"
# default model: text-davinci-003
# response errors: The model `text-davinci-003` has been deprecated.
# They will be shut down on January 04, 2024.
llm = OpenAI(model = "gpt-3.5-turbo-instruct", temperature = 0)

prompt = PromptTemplate.from_template(template)
llm_chain = LLMChain(llm = llm, prompt = prompt)

result = llm_chain("玫瑰")
print(result)
# # result: {'flower': '玫瑰', 'text': '\n\n爱情、美丽、浪漫、温柔、热情、欢乐、尊敬、感激、祝福、纯洁、永恒。'}


# # 2、如果模板中包含多个变量，需要通过JSON字典一次性输入值
# prompt = PromptTemplate(
# 	input_variables = ["flower", "season"],
# 	template = "{flower}在{season}的花语是？")
# llm_chain = LLMChain(llm = llm, prompt = prompt)
# result = llm_chain({ "flower": "玫瑰", "season": "夏季" }) # 默认调用run方法
# print(result)
# # result: {'flower': '玫瑰', 'season': '夏季', 'text': '\n\n夏季的花语是热情、活力、欢乐和爱情。'}


# # 3、predict方法与run方法类型，只是模板变量值通过关键字参数方式输入，而非JSON字典
# result = llm_chain.predict(flower = "梅花", season = "冬季")
# print(result)
# result: 梅花在冬季的花语是坚强、坚持、希望、不屈不挠。它在寒冷的冬季依然能开出美丽的花朵，象征着生命的力量和不畏艰难的精神。同时，梅花也代表着新的开始和希望，预示着春天的到来。

# # 4、apply方法允许一次处理多个输入
# input_list = [
#   { "flower": "玫瑰", "season": "秋季" },
#   { "flower": "郁金香", "season": "夏季" }
# ]
# result = llm_chain.apply(input_list)
# print(result)
# result: [{'text': '\n\n秋季的花语是感恩和收获。'}, {'text': '\n\n夏季的郁金香花语是“热情、欢乐、美丽”。它代表着夏日的热情和欢乐，也象征着美丽的爱情和友谊。'}]


# # 5、generate方法与apply类似，不过它返回一个LLMResult对象，而不是字符串
# result = llm_chain.generate(input_list)
# print(result)
# result: generations=[[Generation(text='\n\n秋季的花语是感恩和收获。', generation_info={'finish_reason': 'stop', 'logprobs': None})], [Generation(text='\n\n夏季的郁金香花语是“热情、欢乐、美丽”。它代表着夏日的热情和欢乐，也象征着美丽的爱情和友谊。', generation_info={'finish_reason': 'stop', 'logprobs': None})]] llm_output={'token_usage': {'prompt_tokens': 32, 'total_tokens': 118, 'completion_tokens': 86}, 'model_name': 'gpt-3.5-turbo-instruct'} run=[RunInfo(run_id=UUID('4b66d907-34b7-4c02-b059-739724817fcf')), RunInfo(run_id=UUID('11f23589-8391-4e79-9c5e-5b64f88e30f9'))]

