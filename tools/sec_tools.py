# SEC 파일 데이터 접근 도구
# SEC 데이터 수집 및 분석 도구
from langchain.tools import tool

class SECTools():
    @tool("10-Q 데이터 수집")
    def search_10q(company):
        """
        주어진 회사의 10-Q 데이터를 수집합니다.
        """
        # 10-Q 데이터 수집 로직을 추가하세요
        return f"{company}의 10-Q 데이터"

    @tool("10-K 데이터 수집")
    def search_10k(company):
        """
        주어진 회사의 10-K 데이터를 수집합니다.
        """
        # 10-K 데이터 수집 로직을 추가하세요
        return f"{company}의 10-K 데이터"
