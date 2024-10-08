# 거시 경제 데이터 수집 도구
# 거시 경제 데이터를 수집하는 도구
from langchain.tools import tool

class EconomicTools():
    @tool("거시 경제 데이터 수집")
    def fetch_macro_data(indicator):
        """
        주어진 경제 지표의 데이터를 수집합니다.
        예를 들어, GDP, 실업률, 인플레이션 등의 지표를 수집할 수 있습니다.
        """
        # 경제 데이터 수집 로직을 추가하세요
        return f"{indicator} 데이터"
