import unittest
import sys
import os

# 현재 디렉토리의 상위 디렉토리를 모듈 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.browser_tools import BrowserTools

class TestBrowserTools(unittest.TestCase):
    def test_scrape_website(self):
        url = "https://donofan.org/?p=99"
        result = BrowserTools.scrape_website(url)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        print(result)

    def test_summarize_text(self):
        url = "https://donofan.org/?p=99"
        text = BrowserTools.scrape_website(url)  # 스크래핑한 텍스트 사용
        result = BrowserTools.summarize_text(text)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        print(result)

if __name__ == '__main__':
    unittest.main()