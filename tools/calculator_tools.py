# 수학 계산 도구
# 수학적 계산 도구
from langchain.tools import tool

class CalculatorTools():
    @tool("계산 수행")
    def calculate(operation):
        """
        어떤 수학적 계산을 수행하는 데 유용합니다.
        덧셈, 뺄셈, 곱셈, 나눗셈 등을 포함합니다.
        이 도구의 입력은 수학적 표현이어야 합니다.
        예를 들어, `200*7` 또는 `5000/2+10`과 같은 식입니다.
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "오류: 수학적 표현에서 문법 오류가 발생했습니다."
