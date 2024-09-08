# My Directions API

이 프로젝트는 **Naver**와 **Kakao 지도 API**를 사용하여 두 지점 간의 경로를 계산하는 **Flask 기반 API**입니다. 두 서비스에서 제공하는 경로를 비교하여 **예상 시간이 더 짧은 경로**를 반환합니다. **MongoDB**를 사용하여 요청 및 응답 데이터를 저장합니다.

## 사전 요구사항

프로젝트를 실행하기 전에 다음 소프트웨어가 설치되어 있어야 합니다:

- **Python** (3.x 버전)
- **Flask**
- **MongoDB** (로컬에 설치하거나 [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) 사용)

로컬에서 **MongoDB**를 사용할 경우, [공식 MongoDB 설치 가이드](https://www.mongodb.com/try/download/community)를 참조하여 설치하세요.

## 설치 방법

1. 이 저장소를 클론합니다:

   ```bash
   git clone https://github.com/your-username/my-directions-api.git
   cd my-directions-api
   ```

2. 가상 환경을 생성하고 활성화합니다:

   ```bash
   # 가상 환경 생성
   python -m venv venv

   # 가상 환경 활성화 (Windows)
   venv\Scripts\activate

   # 가상 환경 활성화 (macOS/Linux)
   source venv/bin/activate
   ```

3. 필요한 Python 패키지를 설치합니다:

   ```bash
   pip install -r requirements.txt
   ```

4. **MongoDB** 설정:
   - **로컬 MongoDB**를 사용하는 경우, MongoDB가 실행 중인지 확인하세요 (기본적으로 `mongodb://localhost:27017`에서 실행됩니다).
   - **MongoDB Atlas**를 사용하는 경우, 클러스터를 생성하고 연결 문자열을 복사한 후 `.env` 파일에 추가하세요.

## 환경 변수 설정

`.env` 파일을 프로젝트 루트 디렉토리에 생성하여, **API 키**와 **MongoDB 연결 정보**를 설정해야 합니다. 아래는 `.env` 파일의 예시입니다:

```bash
NAVER_API_KEY_ID=your_naver_api_key_id
NAVER_API_KEY_SECRET=your_naver_api_key_secret
KAKAO_API_KEY=your_kakao_api_key
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/my_database
```

이 파일에서 API 키 및 MongoDB URI를 적절하게 수정하여 사용합니다.

## API 요청 형식

- **HTTP 메서드**: `POST`
- **URL**: `http://127.0.0.1:5000/directions`

### 요청 예시:

```json
{
    "start": [37.5665, 126.9780],  # 서울 시청 좌표
    "goal": [37.2635, 127.0286]    # 수원 시청 좌표
}
```

### 응답 예시:

```json
{
    "service": "Naver",
    "duration": 3600  # 예상 소요 시간 (초 단위)
}
```

## 사용 방법

서버를 실행한 후, **Postman** 또는 **curl**을 사용하여 경로를 요청할 수 있습니다. 예를 들어, curl을 사용하여 요청하는 방법은 다음과 같습니다:

```bash
curl -X POST http://127.0.0.1:5000/directions -H "Content-Type: application/json" -d "{\"start\": [37.5665, 126.9780], \"goal\": [37.2635, 127.0286]}"
```

이 명령어를 사용하면 **서울 시청**에서 **수원 시청**까지의 경로를 계산하여 응답을 받습니다.
