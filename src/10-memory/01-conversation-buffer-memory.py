#!/usr/bin/env python3

# 要点：ConversationBufferMemory会将所有的聊天历史记录下来，然后加到prompt里面一起传给模型
# 缺点：随着聊天的进行，token会消耗越多，或者达到token限制

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(temperature = 0.5, model_name = "gpt-3.5-turbo-instruct")
conv_chain = ConversationChain(llm = llm)
print(conv_chain.prompt.template)
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

# Current conversation:
# {history}
# Human: {input}
# AI:

from langchain.chains.conversation.memory import ConversationBufferMemory
conversation = ConversationChain(llm = llm, memory = ConversationBufferMemory())

conversation("我姐姐明天过生日，我需要准备一份礼物。")
print("第一次对话后的记忆：", conversation.memory.buffer)
# 第一次对话后的记忆： Human: 我姐姐明天过生日，我需要准备一份礼物。
# AI:  Oh, that's exciting! Birthdays are always a special occasion. Let me see, based on your sister's interests and preferences, I would recommend getting her a nice piece of jewelry or a gift certificate to her favorite store. Or, if she's into experiences, you could plan a fun day out for the two of you, like going to a spa or trying a new activity together. Is there anything specific she has mentioned wanting or something she enjoys doing? That might help me give more personalized suggestions.
conversation("她喜欢惊喜和拆礼盒。")
print("第二次对话后的记忆：", conversation.memory.buffer)
# 第二次对话后的记忆： Human: 我姐姐明天过生日，我需要准备一份礼物。
# AI:  Oh, that's exciting! Birthdays are always a special occasion. Let me see, based on your sister's interests and preferences, I would recommend getting her a nice piece of jewelry or a gift certificate to her favorite store. Or, if she's into experiences, you could plan a fun day out for the two of you, like going to a spa or trying a new activity together. Is there anything specific she has mentioned wanting or something she enjoys doing? That might help me give more personalized suggestions.
# Human: 她喜欢惊喜和拆礼盒。
# AI:  Ah, I see. In that case, you could consider getting her a subscription box for a hobby she enjoys or a surprise trip to a nearby city for a weekend getaway. Another idea could be to create a personalized gift box with small items that have sentimental value to both of you. And don't forget to wrap it in a fun and creative way to add to the surprise factor!

conversation("我又来了，还记得我刚刚说了什么吗？")
print("第三次对话后的记忆：", conversation.memory.buffer)

############### 第二次执行代码后，返回的结果从英文变成中文，另外重新执行代码，不会记住上次执行代码时的对话 ###################
# 第一次对话后的记忆： Human: 我姐姐明天过生日，我需要准备一份礼物。
# AI:  那太好了！生日是一个特殊的日子，我希望你的姐姐能度过一个难忘的生日。你有什么想法准备什么样的礼物呢？我可以帮你提供一些建议。

# 第二次对话后的记忆： Human: 我姐姐明天过生日，我需要准备一份礼物。
# AI:  那太好了！生日是一个特殊的日子，我希望你的姐姐能度过一个难忘的生日。你有什么想法准备什么样的礼物呢？我可以帮你提供一些建议。
# Human: 她喜欢惊喜和拆礼盒。
# AI:  那么我建议你可以准备一个精美的礼盒，里面放上一些她喜欢的小礼物，比如她喜欢的巧克力、香水或者一本书。这样既有惊喜，又可以让她拆礼盒的过程变得更加有趣。你觉得这个主意如何？

# 第三次对话后的记忆：/n Human: 我姐姐明天过生日，我需要准备一份礼物。
# AI:  那太好了！生日是一个特殊的日子，我希望你的姐姐能度过一个难忘的生日。你有什么想法准备什么样的礼物呢？我可以帮你提供一些建议。
# Human: 她喜欢惊喜和拆礼盒。
# AI:  那么我建议你可以准备一个精美的礼盒，里面放上一些她喜欢的小礼物，比如她喜欢的巧克力、香水或者一本书。这样既有惊喜，又可以让她拆礼盒的过程变得更加有趣。你觉得这个主意如何？
# Human: 我又来了，还记得我刚刚说了什么吗？
# AI:  当然记得！你刚刚说你姐姐喜欢惊喜和拆礼盒，我建议你可以准备一个精美的礼盒，里面放上一些她喜欢的小礼物，比如巧克力、香水或者一本书。这样既有惊喜，又可以让她拆礼盒的过程变得更加有趣。你觉得这个主意如何？


