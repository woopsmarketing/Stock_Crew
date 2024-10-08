# 뉴스 데이터 수집 및 분석 도구
# 뉴스 데이터를 수집하고 분석하는 도구
from langchain.tools import tool

class NewsTools():
    @tool("최신 뉴스 가져오기")
    def get_latest_news(topic):
        """
        주어진 주제에 대한 최신 뉴스를 가져옵니다.
        """
        # 뉴스 수집 로직을 추가하세요
        return f"{topic}에 대한 최신 뉴스"
