import requests
from config.config import Config
from requests.exceptions import RequestException
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)

def get_naver_directions(start, goal, option="trafast"):
    """
    Naver 지도 API를 호출하여 경로 정보를 반환합니다.
    
    Parameters:
    - start (tuple): 출발지 (위도, 경도)
    - goal (tuple): 도착지 (위도, 경도)
    - option (str): 경로 탐색 옵션 ('trafast', 'tracomfort', 'traoptimal' 등)

    Returns:
    - dict: currentDateTime, message, summary, routes 정보를 포함한 딕셔너리
    """
    start_lat, start_lng = start
    goal_lat, goal_lng = goal

    # Naver API 엔드포인트
    url = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving"

    # 요청할 파라미터 설정
    params = {
        "start": f"{start_lng},{start_lat}",
        "goal": f"{goal_lng},{goal_lat}",
        "option": option
    }

    # 헤더에 API 키 추가
    headers = {
        "X-NCP-APIGW-API-KEY-ID": Config.NAVER_API_KEY_ID,
        "X-NCP-APIGW-API-KEY": Config.NAVER_API_KEY_SECRET
    }
    
    try:
        # GET 요청 보내기
        logging.info(f"Requesting directions from {start} to {goal} with option {option}")
        response = requests.get(url, params=params, headers=headers)

        # 상태 코드가 200이 아닌 경우 예외 발생
        response.raise_for_status()

        # 응답 JSON 데이터 파싱
        response_data = response.json()

        # 필요한 데이터 추출
        current_date_time = response_data.get('currentDateTime')
        message = response_data.get('message')

        # 경로 정보에서 summary와 path 추출
        routes_data = response_data.get('route', {}).get('trafast', [])
        if routes_data:
            summary = routes_data[0].get('summary', {})
            routes = routes_data[0].get('path', [])
        else:
            summary = {}
            routes = []

        # 응답 데이터 반환
        return {
            "current_date_time": current_date_time,
            "message": message,
            "summary": summary,  # 소요 시간 등의 요약 정보
            "routes": routes      # 좌표 정보 등
        }

    except RequestException as e:
        logging.error(f"Error fetching directions: {e}")
        return {"error": str(e)}