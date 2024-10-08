# CREW AI 메인 진입점
# 이부분을 테스트로 변경해볼것이다.
from crewai import Crew
from agents import StockAnalysisAgents
from tasks import StockAnalysisTasks
from auth import authenticate_user
from config import load_config
from textwrap import dedent

class StockCrew:
    def __init__(self, company):
        self.company = company

    def run(self):
        # 에이전트와 작업을 설정합니다.
        stock_agents = StockAnalysisAgents()
        stock_tasks = StockAnalysisTasks()

        research_analyst_agent = stock_agents.research_analyst()
        financial_analyst_agent = stock_agents.financial_analyst()
        investment_advisor_agent = stock_agents.investment_advisor()
        economic_analyst_agent = stock_agents.economic_analyst()
        political_analyst_agent = stock_agents.political_analyst()

        research_task = stock_tasks.research(research_analyst_agent, self.company)
        financial_task = stock_tasks.financial_analysis(financial_analyst_agent)
        filings_task = stock_tasks.filings_analysis(financial_analyst_agent)
        recommend_task = stock_tasks.recommend(investment_advisor_agent)
        macro_task = stock_tasks.macro_economic_analysis(economic_analyst_agent)
        political_event_task = stock_tasks.political_event_analysis(political_analyst_agent)
        policy_change_task = stock_tasks.policy_change_analysis(political_analyst_agent)
        political_risk_task = stock_tasks.political_risk_assessment(political_analyst_agent)

        # Crew 객체를 생성하고 에이전트와 작업을 할당합니다.
        crew = Crew(
            agents=[
                research_analyst_agent,
                financial_analyst_agent,
                investment_advisor_agent,
                economic_analyst_agent,
                political_analyst_agent
            ],
            tasks=[
                research_task,
                financial_task,
                filings_task,
                recommend_task,
                macro_task,
                political_event_task,
                policy_change_task,
                political_risk_task
            ],
            verbose=True
        )

        # Crew를 실행하고 결과를 반환합니다.
        result = crew.kickoff()
        return result

def main():
    load_config()  # 환경 변수를 로드합니다.

    # 사용자 인증을 진행합니다.
    if not authenticate_user():
        print("인증 실패. 프로그램을 종료합니다.")
        return

    print("## 주식 분석 크루AI에 오신 것을 환영합니다")
    print('-----------------------------------------------')
    
    # 사용자로부터 분석할 회사를 입력받습니다.
    company = input(dedent("""분석할 회사는 무엇입니까?\n"""))

    stock_crew = StockCrew(company)
    result = stock_crew.run()
    print("\n\n########################")
    print("## 여기 분석 결과가 있습니다")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    main()
