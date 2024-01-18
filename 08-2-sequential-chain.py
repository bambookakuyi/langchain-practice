#!usr/bin/env python3

from dotenv import load_dotenv
load_dotenv()

# 目标：使用Sequential Chain把几个LLMChain串起来，形成一个顺序链
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# 1、添加第一个LLMChain，生成鲜花的知识性说明
llm = OpenAI(model = "gpt-3.5-turbo-instruct", temperature = 0.7)
template = """
你是一个植物学家。给定花的名称和类型，你需要为这种花写一个200字左右的介绍。
花名: {name}
颜色: {color}
植物学家: 这是关于上述花的介绍:
"""
prompt_template = PromptTemplate(input_variables = ["name", "color"], template = template)
introduction_chain = LLMChain(llm = llm, prompt = prompt_template, output_key = "introduction")

# 2、添加第二个LLMChain，根据鲜花的知识性说明生成评论
template = """
你是一位鲜花评论家。给定一种花的介绍，你需要为这种花写一篇200字左右的评论。
鲜花介绍:{introduction}
花评人对上述花的评论:
"""
prompt_template = PromptTemplate(input_variables = ["introduction"], template = template)
review_chain = LLMChain(llm = llm, prompt = prompt_template, output_key = "review")

# 3、添加第三个LLMChain，根据鲜花的介绍和评论写出一篇自媒体文案
template = """
你是一家花店的社交媒体经理。给定一种花的介绍和评论，你需要为这种花写一篇社交媒体的帖子，300字左右。
鲜花介绍:{introduction}
花评人对上述花的评论:{review}
社交媒体帖子:
"""
prompt_template = PromptTemplate(input_variables = ["introduction", "review"], template = template)
social_post_chain = LLMChain(llm = llm, prompt = prompt_template, output_key = "social_post_text")

# 4、最后添加SequentialChain，把三个链串起来
overall_chain = SequentialChain(
	chains = [introduction_chain, review_chain, social_post_chain],
	input_variables = ["name", "color"],
	output_variables = ["introduction", "review", "social_post_text"],
	verbose = True
)

result = overall_chain({ "name": "玫瑰", "color": "黑色" })
print(result)
# reesult after format:
# {
#     'name': '玫瑰',
#     'color': '黑色',
#     'introduction': '\n玫瑰是一种美丽的花卉，也被称为花中皇后。它是蔷薇科的一种植物，通常生长在温暖和温和的气候下。它们可以在各种颜色中找到，但黑色玫瑰却是最为稀有和神秘的一种。\n\n黑色玫瑰具有深邃的美感，它们散发出一种神秘的魅力，让人们无法抗拒。它们的花瓣呈现出深黑色，有时甚至带有紫色或暗红色的色调。这种独特的颜色使得黑色玫瑰成为许多人心中的梦想花朵。\n\n除了其美丽的外表，黑色玫瑰也有着丰',
#     'review': '\n黑色玫瑰，一种神秘而美丽的花朵。它散发着深邃的魅力，让人们无法抗拒。无论是在花园中还是在花束中，它都能吸引所有人的目光。\n\n首先，黑色玫瑰的花瓣呈现出深黑色，散发着一种神秘的气息。有时，它们还会带有紫色或暗红色的色调，为花朵增添了一份神秘感。这种独特的颜色让黑色玫瑰成为许多人心中的梦想花朵，也是花艺师们最喜爱的创作素材。\n\n其次，黑色玫瑰所代表的意义也是令人心动的。它象征',
#     'social_post_text': '\n大家好！今天我想和大家分享一种神秘而美丽的花卉，它被誉为花中皇后，也是许多人心中的梦想花朵。是的，我说的就是黑色玫瑰。\n\n黑色玫瑰，一种散发着深邃魅力的花朵，它的花瓣呈现出深黑色，有时还带有紫色或暗红色的色调，让人们无法抗拒。它们生长在温暖和温和的气候下，是蔷薇科的一种植物。除了美丽的外表，黑色玫瑰也有着丰富的意义。它象征着神
#     秘、浪漫和独特，是许多人心中的理想花'
# }