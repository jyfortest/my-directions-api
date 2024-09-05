import requests
from config.api_keys import NAVER_API_KEY

def get_naver_directions(lat, lng):
  response = requests.get()