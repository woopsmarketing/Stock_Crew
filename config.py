# 프로젝트 설정 파일
# 프로젝트 설정 파일
import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()  # .env 파일을 로드하여 환경 변수를 설정합니다.
    # 추가 설정이 필요한 경우 여기에 추가합니다