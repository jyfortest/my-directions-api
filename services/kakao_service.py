import requests
from config.config import Config  # API 키를 환경 변수에서 가져옴
from requests.exceptions import RequestException
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)

def get_kakao_directions(start, goal):
    """
    Kakao Maps 자동차 경로 탐색 API를 호출하여 경로 정보를 반환합니다.
    
    Parameters:
    - start (tuple): 출발지 (위도, 경도)
    - goal (tuple): 도착지 (위도, 경도)

    Returns:
    - dict: 경로 탐색 결과 (요약 정보 및 경로 좌표)
    """
    # Kakao Maps 경로 탐색 API 엔드포인트
    url = "https://apis-navi.kakaomobility.com/v1/directions"
    
    # 경로 탐색을 위한 파라미터 설정
    params = {
        "origin": f"{start[1]},{start[0]}",  # 경도, 위도 순서
        "destination": f"{goal[1]},{goal[0]}",  # 경도, 위도 순서
        "priority": "RECOMMEND"  # 추천 경로 옵션
    }

    # 요청 시 사용할 헤더 (API 인증)
    headers = {
        "Authorization": f"KakaoAK {Config.KAKAO_API_KEY}"  # Kakao API 키 인증
    }

    try:
        # API 요청 보내기
        logging.info(f"Requesting Kakao directions from {start} to {goal}")
        response = requests.get(url, params=params, headers=headers)

        # 응답 상태 코드 확인
        response.raise_for_status()

        # JSON 응답 파싱
        response_data = response.json()

        # 경로 요약 정보 및 좌표 추출
        summary = response_data.get('routes', [])[0].get('summary', {})
        path = response_data.get('routes', [])[0].get('sections', [])[0].get('roads', [])[0].get('vertexes', [])

        return {
            "summary": summary,  # 소요 시간, 거리 등의 요약 정보
            "path": path         # 경로 좌표 정보
        }

    except RequestException as e:
        logging.error(f"Error fetching Kakao directions: {e}")
        return {"error": str(e)}