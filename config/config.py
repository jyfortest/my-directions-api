import os

class Config:
    NAVER_API_KEY_ID = os.getenv('NAVER_API_KEY_ID')
    NAVER_API_KEY_SECRET = os.getenv('NAVER_API_KEY_SECRET')
    KAKAO_API_KEY = os.getenv('KAKAO_API_KEY')
    MONGO_URI = os.getenv('MONGO_URI')