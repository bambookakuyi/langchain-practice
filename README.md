# langchain-practice

《极客时间》黄佳讲授的《LangChain 实战课》每讲练习

## LangChain 简介
LangChain是全方位的基于大语言模型的应用开发框架。  
大模型，学术上更多被称作基础模型（foundation model 或 base model），是一种通过深度学习技术以达到理解并生成人类语言的人工智能。之所以是”大“模型，具体体现在训练数据量大，参数量大，迁移能力强（即下游任务多）。下游任务包括知识问答、图片生成、情感分析、目标检测等。

## 环境变量
根目录添加.env文件, 文件添加内容：
```python
OPENAI_API_KEY = "Your OpenAI API key"
```

## 目录结构
每一讲的练习用例都放在根目录中，文件标题前面的序号表示第几讲。  
有一些例子需要用到文章、图片等资源文件，会放在static目录中。

## 执行用例
Mac OS中, 可以在python脚本文件首行添加注释`#!/usr/bin/env python3`，然后在终端输入命令`chmod a+x 文件名`添加执行权限, 最后输入命令`./文件名`执行代码。部分用例，比如`02-one-flower`是一个mini web，需要通过Flask来启动服务，具体可查看文件中的注释。
