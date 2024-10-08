# 인터넷 검색 도구
# 인터넷 검색 도구
import requests
from langchain.tools import tool
import os
import json

class SearchTools():
    @tool("인터넷 검색")
    def search_internet(query):
        """
        주어진 주제에 대해 인터넷을 검색하고 관련 결과를 반환하는 데 유용합니다.
        """
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if 'organic' not in response.json():
            return "죄송합니다, 해당 주제에 대한 정보를 찾을 수 없습니다. Serper API 키에 문제가 있을 수 있습니다."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"제목: {result['title']}", f"링크: {result['link']}",
                        f"요약: {result['snippet']}", "\n-----------------"
                    ]))
                except KeyError:
                    continue
            return '\n'.join(string)
