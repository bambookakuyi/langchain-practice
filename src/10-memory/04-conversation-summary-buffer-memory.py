#!usr/bin/env python3

# 要点：ConversationSummaryBufferMemory是对话总结缓冲记忆。
# 优点：这种模型旨在在对话中总结早期的互动，同时尽量保留最近互动中的原始内容

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryBufferMemory
from time import sleep
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(temperature = 0.5, model_name = "gpt-3.5-turbo-instruct")
conversation = ConversationChain(
	llm = llm,
	memory = ConversationSummaryBufferMemory(
	  llm = llm,
	  # 当最新的对话文字长度在 300 字之内的时候，LangChain 会记忆原始对话内容；当对话文字超出了这个参数的长度，那么模型就会把所有超过预设长度的内容进行总结，以节省 Token 数量
	  max_token_limit = 300
	)
)
result = conversation("我姐姐明天过生日，我需要准备一份礼物。")
print(result)
# {
#     'input': '我姐姐明天过生日，我需要准备一份礼物。',
#     'history': '',
#     'response': ' 那真是太好了，祝你姐姐生日快乐！我可以帮你提供一些礼物建议。根据我所知，你的姐姐喜欢旅行，所以你可以考虑送她一本旅行指南书或者一张旅行卡。如果她喜欢美食，你也可以送她一份美食礼篮或者预订一顿特别的餐厅。另外，你也可以考虑送她一件她喜欢的服装或者配饰，或者一份她想要很久的东西。你有什么想法吗？'
# }

sleep(55) # 55.seconds
result = conversation("她喜欢时尚的衣服、首饰，你有什么比较优惠的品牌推荐吗？")
print(result)
# {
#     'input': '她喜欢时尚的衣服、首饰，你有什么比较优惠的品牌推荐吗？',
#     'history': 'Human: 我姐姐明天过生日，我需要准备一份礼物。\nAI:  那真是太好了，祝你姐姐生日快乐！我可以帮你提供一些礼物建议。根据我所知，你的姐姐喜欢旅行，所以你可以考虑送她一本旅行指南书或者一张旅行卡。如果她喜欢美食，你也可以送她一份美食礼篮或者预订一顿特别的餐厅。另外，你也可以考虑送她一件她喜欢的服装或者配饰，或者一份她想要很久的东西。你有什么想法吗？',
#     'response': ' 当然，我可以为你推荐一些时尚的品牌。如果你想要高档的品牌，你可以考虑Gucci、Louis Vuitton或者Chanel。如果你想要更实惠一些的品牌，你可以看看Zara、H&M或者Forever 21。另外，如果你想要更具个性的品牌，你可以考虑Urban Outfitters或者Free People。希望这些推荐能帮到你！'
# }

sleep(55) # 55.seconds
result = conversation("我又来了，还记得我要做什么吗？")
print(result)
# {
#     'input': '我又来了，还记得我要做什么吗？',
#     'history': "System: The human tells the AI that their sister's birthday is tomorrow and they need to prepare a gift. The AI offers to provide gift suggestions and mentions that the sister likes traveling. The AI suggests a travel guidebook or a travel gift card as potential gifts. It also suggests a food gift basket or a reservation at a special restaurant if the sister likes food. Other gift ideas include clothing, accessories, or something the sister has been wanting for a long time. The AI asks the human if they have any ideas.\nHuman: 她喜欢时尚的衣服、首饰，你有什么比较优惠的品牌推荐吗？\nAI:  当然，我可以为你推荐一些时尚的品牌。如果你想要高档的品牌，你可以考虑Gucci、Louis Vuitton或者Chanel。如果你想要更实惠一些的品牌，你可以看看Zara、H&M或者Forever 21。另外，如果你想要更具个性的品牌，你可以考虑Urban Outfitters或者Free People。希望这些推荐能帮到你！",
#     'response': ' 当然，你要为你妹妹准备生日礼物。我还记得她喜欢旅行，所以我建议你可以考虑一本旅行指南书或者旅行礼品卡作为礼物。如果她喜欢美食，你也可以考虑一个美食礼篮或者预订一家特别的餐厅。其他的礼物想法包括服装、配饰，或者她长期想要的东西。你有什么想法吗？'
# }
