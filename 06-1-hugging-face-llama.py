#!/usr/bin/env python3

# 用 HuggingFace 跑开源模型
from transformers import AutoTokenizer, AutoModelForCausalLM # pip3 install transformers

# 加载预训练模型的分词器
tokenizer = AutoTokenizer.from_pretrained("meta-llama/llama-2-7b-chat-hf")

# 加载预训练的模型
# 使用 device_map 参数将模型自动加载到可用的硬件设备上，比如GPU
model = AutoModelForCasualLM.from_pretrained(
  "meta-llama/llama-2-7b-chat-hf",
  device_map = auto)

prompt = "请给我讲个玫瑰花的爱情故事"

# 使用分词器将提示转化为模型可以理解的格式
# .to("cuda") 表示将格式化的提示移到GPU上，如果是在CPU上运行，则取掉该选项
inputs = tokenizer(prompt, return_tensors = "pt").to("cuda")

# 使用模型生成文本，设置最大生成令牌数为2000
outputs = model.generae(inputs["input_ids"], max_new_tokens = 2000)

# 将生成的令牌解码成文本，并跳过任何特殊的令牌，例如[CLS], [SEP]等
response = tokenizer.decode(outputs[0], skip_special_tokens = True)
print(response)
