#!/usr/bin/env python3

# pip3 install playwright
# playwright install # 安装 Chromium, FFMPEG, Firefox和Webkit
from playwright.sync_api import sync_playwright

def run():
	# 使用Playwrite上下文管理器
	with sync_playwright() as p:
		browser = p.chromium.launch()
		page = browser.new_page()
		page.goto("https://langchain.com/")
		title = page.title()
		print(f"Page title is: {title}")
		# Page title is: LangChain
		browser.close()

if __name__ == "__main__":
	run()