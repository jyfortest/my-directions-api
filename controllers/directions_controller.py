from services.naver_service import get_naver_directions
from services.kakao_service import get_kakao_directions
from config.db import db
import datetime

def get_shortest_route(start, goal):
    #Naver 경로 요청
    naver_result = get_naver_directions(start, goal)
    naver_duration = naver_result['summary'].get('duration', float('inf'))
    
    #kakao 경로 요청
    kakao_result = get_kakao_directions(start, goal)
    kakao_duration = kakao_result['summary'].get('duration', float('inf'))

    route_data = {
        "start" : start,
        "goal" : goal,
        "naver_result": naver_result,
        "kakao_result": kakao_result,
        "timestamp": datetime.datetime.utcnow()
    }

    if naver_duration < kakao_duration:
        selected_server = "Naver"

    else :
        selected_server = "Kakao"

    #저장할 정보에 선택 된 서버 정보 추가
    route_data.update({
        "selected_server" : selected_server
    })

    db['routes'].insert_one(route_data)

    return {
        "service": selected_server,
        "duration": min(naver_duration, kakao_duration)
    }