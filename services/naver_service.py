import requests
from config.api_keys import NAVER_API_KEY

def get_naver_directions(start, goal, option="trafast"):
  # start와 goal은 (lat, lng) 형태의 tuple
  start_lat, start_lng = start
  goal_lat, goal_lng = goal

  # Naver API 엔드포인트
  url = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving"

  params = {
    "start": f"{start_lng},{start_lat}",
    "goal": f"{goal_lng},{goal_lat}",
    "option" : option
  }

  headers = {
    "X-NCP-APIGW-API-KEY-ID": NAVER_API_KEY,
    "X-NCP-APIGW-API_KEY": NAVER_API_KEY
  }

  response = requests.get(url, params=params, headers=headers)

  if response.status_code == 200:
      response_data = response.json()

      current_data_time = response_data.get('currentDateTime')
      message = response_data.get('message')
      route = response_data.get('route', {})

      #모든 데이터를 하나의 딕서녀리로 반환
      return{
         "currentDateTime": current_data_time,
         "message": message,
         "route": route
      }
  else:
     return{"error": response.json()}