# 주식 분석을 위한 다양한 에이전트를 정의
# 주식 분석을 위한 다양한 에이전트를 정의
from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools
from tools.economic_tools import EconomicTools
from tools.chart_tools import ChartTools
from tools.risk_tools import RiskTools
from tools.esg_tools import ESGTools
from tools.news_tools import NewsTools
from tools.social_media_tools import SocialMediaTools
from tools.political_tools import PoliticalTools

class StockAnalysisAgents():
    def financial_analyst(self):
        """
        재무 분석 에이전트를 생성합니다.
        역할: 주식 시장 분석 및 투자 전략 제공
        목표: 고객에게 재무 데이터와 시장 트렌드 분석 제공
        배경 스토리: 많은 경험을 가진 재무 분석가
        도구: 웹 스크래핑, 인터넷 검색, 계산기, SEC 데이터 분석 도구 사용
        """
        return Agent(
            role='최고의 재무 분석가',
            goal="""고객에게 재무 데이터와 시장 트렌드 분석으로 감동을 주세요""",
            backstory="""다양한 주식 시장 분석과 투자 전략에 능통한 경험 많은 재무 분석가입니다.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                CalculatorTools.calculate,
                SECTools.search_10q,
                SECTools.search_10k
            ]
        )

    def research_analyst(self):
        """
        리서치 분석 에이전트를 생성합니다.
        역할: 데이터를 수집하고 해석하여 고객에게 제공합니다.
        목표: 최고의 데이터를 제공하여 고객을 감동시킵니다.
        배경 스토리: 최고의 리서치 분석가로, 뉴스, 회사 발표, 시장 감정을 분석하는 전문가입니다.
        도구: 웹 스크래핑, 인터넷 검색, 뉴스 검색 도구 사용
        """
        return Agent(
            role='리서치 분석가',
            goal="""데이터를 수집하고 해석하여 최고의 데이터를 제공하여 고객을 감동시키세요""",
            backstory="""뉴스, 회사 발표, 시장 감정을 분석하는 최고의 리서치 분석가입니다.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                SECTools.search_10q,
                SECTools.search_10k
            ]
        )

    def investment_advisor(self):
        """
        투자 상담 에이전트를 생성합니다.
        역할: 주식에 대한 완전한 분석과 투자 권장 사항을 제공합니다.
        목표: 고객에게 종합적인 투자 분석을 제공하고 완벽한 투자 전략을 권장합니다.
        배경 스토리: 다양한 분석 통찰력을 결합하여 전략적 투자 조언을 제공하는 경험 많은 투자 상담사입니다.
        도구: 웹 스크래핑, 인터넷 검색, 뉴스 검색 도구 사용
        """
        return Agent(
            role='개인 투자 상담사',
            goal="""고객에게 완전한 주식 분석과 종합적인 투자 권장 사항을 제공합니다""",
            backstory="""다양한 분석 통찰력을 결합하여 전략적 투자 조언을 제공하는 경험 많은 투자 상담사입니다.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                CalculatorTools.calculate,
                NewsTools.get_latest_news
            ]
        )

    def economic_analyst(self):
        """
        경제 분석 에이전트를 생성합니다.
        역할: 거시 경제 지표를 분석하여 시장 트렌드를 제공합니다.
        목표: 경제 데이터를 분석하여 시장 트렌드에 대한 통찰력을 제공합니다.
        배경 스토리: 경제 데이터를 해석하고 주식 시장에 미치는 영향을 분석하는 전문가입니다.
        도구: 경제 데이터 수집 도구, 데이터 시각화 도구 사용
        """
        return Agent(
            role='경제 분석가',
            goal="""거시 경제 지표를 분석하여 시장 트렌드를 제공합니다""",
            backstory="""경제 데이터를 해석하고 주식 시장에 미치는 영향을 분석하는 전문가입니다.""",
            verbose=True,
            tools=[
                EconomicTools.fetch_macro_data,
                ChartTools.plot_data
            ]
        )

    def political_analyst(self):
        """
        정치 분석 에이전트를 생성합니다.
        역할: 정치 이벤트와 정책 변화를 분석하여 시장에 미치는 영향을 제공합니다.
        목표: 정치 이벤트와 정책 변화를 분석하여 주식 시장에 미치는 영향을 제공합니다.
        배경 스토리: 정치 이벤트가 주식 시장에 미치는 영향을 깊이 이해하는 정치 분석 전문가입니다.
        도구: 정치 데이터 수집 도구, 뉴스 검색 도구, 소셜 미디어 분석 도구 사용
        """
        return Agent(
            role='정치 분석가',
            goal="""정치 이벤트와 정책 변화를 분석하여 주식 시장에 미치는 영향을 제공합니다""",
            backstory="""정치 이벤트가 주식 시장에 미치는 영향을 깊이 이해하는 정치 분석 전문가입니다.""",
            verbose=True,
            tools=[
                PoliticalTools.fetch_political_data,
                NewsTools.get_latest_news,
                SocialMediaTools.analyze_mentions,
                ChartTools.plot_data
            ]
        )
