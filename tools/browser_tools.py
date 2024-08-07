# 웹 스크래핑 및 요약 도구
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

class BrowserTools():
    @tool("웹 스크래핑")
    def scrape_website(url):
        """
        주어진 URL에서 웹 페이지를 스크래핑하고 전체 텍스트를 반환합니다.
        """
        response = requests.get(url)
        if response.status_code != 200:
            return "웹 페이지를 가져오지 못했습니다."

        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([para.get_text() for para in paragraphs])

        return text

    @tool("텍스트 요약")
    def summarize_text(text):
        """
        주어진 텍스트를 요약합니다.
        """
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        if len(text) < 130:
            max_length = len(text)
        else:
            max_length = 130

        summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
        return summary[0]['summary_text']