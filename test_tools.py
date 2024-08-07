import unittest

import os

# 현재 디렉토리의 상위 디렉토리를 모듈 경로에 추가

from tools.browser_tools import BrowserTools

class TestBrowserTools(unittest.TestCase):
    def test_scrape_and_summarize_website(self):
        url = "https://m.blog.naver.com/jang1543/223416520251"
        result = BrowserTools.scrape_and_summarize_website(url)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        print(result)

if __name__ == '__main__':
    unittest.main()
