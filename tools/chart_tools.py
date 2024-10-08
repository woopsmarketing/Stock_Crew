# 차트 및 그래프 도구
# 차트 및 그래프 도구
from langchain.tools import tool
import matplotlib.pyplot as plt
import io
import base64

class ChartTools():
    @tool("데이터 시각화")
    def plot_data(data, chart_type="line"):
        """
        주어진 데이터를 시각화합니다.
        chart_type은 "line", "bar", "scatter" 중 하나일 수 있습니다.
        """
        plt.figure()
        if chart_type == "line":
            plt.plot(data)
        elif chart_type == "bar":
            plt.bar(range(len(data)), data)
        elif chart_type == "scatter":
            plt.scatter(range(len(data)), data)
        else:
            return "오류: 지원하지 않는 차트 유형입니다."
        
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        image_base64 = base64.b64encode(image_png).decode("utf-8")
        
        return image_base64
