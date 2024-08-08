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
        주어진 텍스트를 요약합니다. 텍스트가 길면 모델이 처리할 수 있는 길이로 나누어 처리합니다.
        """
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        max_chunk_length = 1024  # 모델이 처리할 수 있는 최대 토큰 길이

        # 텍스트를 모델이 처리할 수 있는 길이로 나누기
        chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]

        summaries = []
        for chunk in chunks:
            summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])

        # 나누어진 요약본들을 합쳐서 최종 요약본 생성
        final_summary = ' '.join(summaries)
        return final_summary