# at-thirty-rules API 설계 규칙

## 🎯 API 설계 원칙

### 1. RESTful API 설계
- **HTTP 메서드**: GET, POST, PUT, DELETE 적절히 사용
- **리소스 중심**: 명사로 URL 구성
- **상태 코드**: 적절한 HTTP 상태 코드 사용
- **일관성**: 모든 API가 동일한 패턴 따르기

### 2. URL 설계 규칙
```
모든 API는 /api/* 경로로 시작
/api/v1/... (버전 관리)
/api/health (헬스 체크)
/api/chat (채팅)
/api/fortune (사주)
```

## 📋 API 엔드포인트 명세

### 1. 헬스 체크 API

#### `GET /api/health`
```python
@app.get("/api/health")
async def health_check():
    """
    서비스 상태 확인 API
    
    Returns:
        dict: 서비스 상태 정보
    """
    return {
        "reply": "서비스가 정상적으로 실행 중입니다.",
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }
```

**응답 예시:**
```json
{
    "reply": "서비스가 정상적으로 실행 중입니다.",
    "status": "healthy",
    "timestamp": "2024-01-15T10:30:00.000Z"
}
```

### 2. 채팅 API

#### `POST /api/chat`
```python
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    user_id: str = None
    conversation_id: str = None

class ChatResponse(BaseModel):
    reply: str
    conversation_id: str
    timestamp: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """
    AI와 채팅하는 API
    
    Args:
        request (ChatRequest): 채팅 요청 데이터
            - message (str): 사용자 메시지
            - user_id (str, optional): 사용자 ID
            - conversation_id (str, optional): 대화 ID
    
    Returns:
        ChatResponse: AI 응답 데이터
            - reply (str): AI 응답 메시지
            - conversation_id (str): 대화 ID
            - timestamp (str): 응답 시간
    
    Raises:
        HTTPException: API 호출 실패 시
    """
    try:
        # OpenAI API 호출
        ai_response = await openai_service.get_chat_response(
            message=request.message,
            user_id=request.user_id,
            conversation_id=request.conversation_id
        )
        
        return ChatResponse(
            reply=ai_response["content"],
            conversation_id=ai_response["conversation_id"],
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"채팅 처리 중 오류가 발생했습니다: {str(e)}"
        )
```

**요청 예시:**
```json
{
    "message": "안녕하세요! 오늘 운세가 어떤가요?",
    "user_id": "user123",
    "conversation_id": "conv456"
}
```

**응답 예시:**
```json
{
    "reply": "안녕하세요! 오늘은 좋은 날이 될 것 같습니다. 특히 오후에 좋은 소식이 있을 것 같아요.",
    "conversation_id": "conv456",
    "timestamp": "2024-01-15T10:30:00.000Z"
}
```

### 3. 사주 API

#### `POST /api/fortune`
```python
class FortuneRequest(BaseModel):
    birth_date: str  # YYYY-MM-DD 형식
    name: str = None
    birth_time: str = None  # HH:MM 형식 (선택사항)
    gender: str = None  # "male" 또는 "female" (선택사항)

class FortuneResponse(BaseModel):
    reply: str
    fortune_data: dict
    timestamp: str

@app.post("/api/fortune", response_model=FortuneResponse)
async def get_fortune(request: FortuneRequest):
    """
    사주를 조회하는 API
    
    Args:
        request (FortuneRequest): 사주 요청 데이터
            - birth_date (str): 생년월일 (YYYY-MM-DD)
            - name (str, optional): 사용자 이름
            - birth_time (str, optional): 출생 시간 (HH:MM)
            - gender (str, optional): 성별
    
    Returns:
        FortuneResponse: 사주 결과 데이터
            - reply (str): 사주 해석 메시지
            - fortune_data (dict): 상세 사주 데이터
            - timestamp (str): 조회 시간
    
    Raises:
        HTTPException: 잘못된 입력 또는 처리 실패 시
    """
    try:
        # 입력 검증
        if not request.birth_date or len(request.birth_date) != 10:
            raise HTTPException(
                status_code=400, 
                detail="올바른 날짜 형식이 아닙니다 (YYYY-MM-DD)"
            )
        
        # 사주 계산
        fortune_result = await fortune_service.get_fortune(
            birth_date=request.birth_date,
            name=request.name,
            birth_time=request.birth_time,
            gender=request.gender
        )
        
        return FortuneResponse(
            reply=fortune_result["interpretation"],
            fortune_data=fortune_result["data"],
            timestamp=datetime.now().isoformat()
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"사주 조회 중 오류가 발생했습니다: {str(e)}"
        )
```

**요청 예시:**
```json
{
    "birth_date": "1990-01-15",
    "name": "홍길동",
    "birth_time": "14:30",
    "gender": "male"
}
```

**응답 예시:**
```json
{
    "reply": "홍길동님의 사주를 분석한 결과, 금수상생의 좋은 운세를 가지고 계십니다. 특히 올해는 새로운 기회가 많이 찾아올 것 같습니다.",
    "fortune_data": {
        "zodiac_sign": "양",
        "element": "금",
        "score": 85,
        "lucky_numbers": [3, 7, 9],
        "lucky_colors": ["금색", "흰색"],
        "lucky_directions": ["서쪽", "북서쪽"],
        "personality": "성실하고 책임감이 강한 성격",
        "career_advice": "금융이나 기술 분야에서 성공할 가능성이 높습니다",
        "love_advice": "진실한 마음으로 상대방을 대하면 좋은 인연을 만날 수 있습니다"
    },
    "timestamp": "2024-01-15T10:30:00.000Z"
}
```

### 4. 사주 상세 조회 API

#### `GET /api/fortune/{fortune_id}`
```python
@app.get("/api/fortune/{fortune_id}")
async def get_fortune_detail(fortune_id: str):
    """
    특정 사주 결과의 상세 정보를 조회하는 API
    
    Args:
        fortune_id (str): 사주 결과 ID
    
    Returns:
        dict: 사주 상세 정보
    
    Raises:
        HTTPException: 사주 결과를 찾을 수 없을 때
    """
    try:
        fortune_detail = await fortune_service.get_fortune_detail(fortune_id)
        
        if not fortune_detail:
            raise HTTPException(
                status_code=404, 
                detail="해당 사주 결과를 찾을 수 없습니다"
            )
        
        return {
            "reply": "사주 상세 정보를 조회했습니다.",
            "fortune_detail": fortune_detail,
            "timestamp": datetime.now().isoformat()
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"사주 상세 조회 중 오류가 발생했습니다: {str(e)}"
        )
```

## 🔧 API 공통 규칙

### 1. 응답 형식 통일
```python
# 모든 OpenAI 응답은 {"reply": "..."} 형태로 반환
def format_openai_response(content: str) -> dict:
    """
    OpenAI 응답을 표준 형식으로 포맷팅
    
    Args:
        content (str): OpenAI 응답 내용
    
    Returns:
        dict: 표준 응답 형식
    """
    return {"reply": content}
```

### 2. 에러 처리 규칙
```python
from fastapi import HTTPException
from fastapi.responses import JSONResponse

# 공통 에러 응답 형식
def create_error_response(status_code: int, detail: str) -> JSONResponse:
    """
    표준 에러 응답 생성
    
    Args:
        status_code (int): HTTP 상태 코드
        detail (str): 에러 메시지
    
    Returns:
        JSONResponse: 에러 응답
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "reply": f"오류가 발생했습니다: {detail}",
            "error": True,
            "status_code": status_code,
            "timestamp": datetime.now().isoformat()
        }
    )

# 사용 예시
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return create_error_response(400, str(exc))

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return create_error_response(500, "서버 내부 오류가 발생했습니다")
```

### 3. 요청 검증 규칙
```python
from pydantic import BaseModel, validator
from datetime import datetime

class BaseRequest(BaseModel):
    """기본 요청 모델"""
    
    @validator('*', pre=True)
    def validate_strings(cls, v):
        """문자열 필드 검증"""
        if isinstance(v, str) and v.strip() == "":
            raise ValueError("빈 문자열은 허용되지 않습니다")
        return v

class FortuneRequest(BaseRequest):
    birth_date: str
    name: str = None
    
    @validator('birth_date')
    def validate_birth_date(cls, v):
        """생년월일 형식 검증"""
        try:
            datetime.strptime(v, '%Y-%m-%d')
            return v
        except ValueError:
            raise ValueError('날짜 형식이 올바르지 않습니다 (YYYY-MM-DD)')
    
    @validator('name')
    def validate_name(cls, v):
        """이름 검증"""
        if v and len(v.strip()) < 2:
            raise ValueError('이름은 2자 이상이어야 합니다')
        return v
```

### 4. 로깅 규칙
```python
import logging
from datetime import datetime

# 로거 설정
logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request, call_next):
    """API 요청 로깅 미들웨어"""
    start_time = datetime.now()
    
    # 요청 로그
    logger.info(f"API 요청: {request.method} {request.url}")
    
    # 응답 처리
    response = await call_next(request)
    
    # 처리 시간 계산
    process_time = (datetime.now() - start_time).total_seconds()
    
    # 응답 로그
    logger.info(
        f"API 응답: {response.status_code} "
        f"처리시간: {process_time:.3f}초"
    )
    
    return response
```

## 🧪 API 테스트 규칙

### 1. curl 테스트 스크립트
```bash
#!/bin/bash
# api_test.sh - API 테스트 스크립트

BASE_URL="http://localhost:8000"

echo "=== at-thirty-rules API 테스트 ==="

# 1. 헬스 체크 테스트
echo "1. 헬스 체크 테스트"
curl -X GET "${BASE_URL}/api/health" \
     -H "Content-Type: application/json" \
     -w "\nHTTP Status: %{http_code}\n\n"

# 2. 채팅 API 테스트
echo "2. 채팅 API 테스트"
curl -X POST "${BASE_URL}/api/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "안녕하세요! 오늘 운세가 어떤가요?",
       "user_id": "test_user_001",
       "conversation_id": "conv_001"
     }' \
     -w "\nHTTP Status: %{http_code}\n\n"

# 3. 사주 API 테스트
echo "3. 사주 API 테스트"
curl -X POST "${BASE_URL}/api/fortune" \
     -H "Content-Type: application/json" \
     -d '{
       "birth_date": "1990-01-15",
       "name": "홍길동",
       "birth_time": "14:30",
       "gender": "male"
     }' \
     -w "\nHTTP Status: %{http_code}\n\n"

# 4. 잘못된 요청 테스트
echo "4. 잘못된 요청 테스트"
curl -X POST "${BASE_URL}/api/fortune" \
     -H "Content-Type: application/json" \
     -d '{
       "birth_date": "invalid-date",
       "name": "홍길동"
     }' \
     -w "\nHTTP Status: %{http_code}\n\n"

echo "=== API 테스트 완료 ==="
```

### 2. Python 테스트 코드
```python
import pytest
import httpx
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    """헬스 체크 API 테스트"""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert "reply" in data
    assert data["status"] == "healthy"

def test_chat_api():
    """채팅 API 테스트"""
    response = client.post("/api/chat", json={
        "message": "안녕하세요!",
        "user_id": "test_user"
    })
    assert response.status_code == 200
    data = response.json()
    assert "reply" in data
    assert "conversation_id" in data

def test_fortune_api():
    """사주 API 테스트"""
    response = client.post("/api/fortune", json={
        "birth_date": "1990-01-15",
        "name": "홍길동"
    })
    assert response.status_code == 200
    data = response.json()
    assert "reply" in data
    assert "fortune_data" in data

def test_invalid_birth_date():
    """잘못된 날짜 형식 테스트"""
    response = client.post("/api/fortune", json={
        "birth_date": "invalid-date",
        "name": "홍길동"
    })
    assert response.status_code == 400
    data = response.json()
    assert "오류가 발생했습니다" in data["reply"]
```

## 📊 API 문서화 규칙

### 1. Swagger/OpenAPI 자동 문서화
```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

def custom_openapi():
    """커스텀 OpenAPI 스키마 생성"""
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="at-thirty-rules API",
        version="1.0.0",
        description="사주 검색 및 채팅 서비스 API",
        routes=app.routes,
    )
    
    # 커스텀 정보 추가
    openapi_schema["info"]["x-logo"] = {
        "url": "https://example.com/logo.png"
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

### 2. API 명세서 작성 규칙
```markdown
## API 명세서

### 기본 정보
- **Base URL**: `https://api.at-thirty-rules.com`
- **API 버전**: v1
- **인증**: API Key (Header: `X-API-Key`)

### 엔드포인트 목록

#### 1. 헬스 체크
- **URL**: `GET /api/health`
- **설명**: 서비스 상태 확인
- **응답**: 서비스 상태 정보

#### 2. 채팅
- **URL**: `POST /api/chat`
- **설명**: AI와 채팅
- **요청**: 메시지, 사용자 ID, 대화 ID
- **응답**: AI 응답, 대화 ID, 타임스탬프

#### 3. 사주 조회
- **URL**: `POST /api/fortune`
- **설명**: 사주 정보 조회
- **요청**: 생년월일, 이름, 출생시간, 성별
- **응답**: 사주 해석, 상세 데이터, 타임스탬프
```

## 🔒 보안 규칙

### 1. API 키 관리
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """API 키 검증"""
    if credentials.credentials != os.getenv("API_KEY"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 API 키입니다"
        )
    return credentials.credentials

# 사용 예시
@app.post("/api/chat")
async def chat_with_ai(
    request: ChatRequest,
    api_key: str = Depends(verify_api_key)
):
    # API 로직
    pass
```

### 2. 요청 제한 (Rate Limiting)
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/api/chat")
@limiter.limit("10/minute")  # 분당 10회 제한
async def chat_with_ai(request: Request, chat_request: ChatRequest):
    # API 로직
    pass
```

## 📋 API 개발 체크리스트

### 개발 시
- [ ] 모든 API가 `/api/*` 경로로 시작하는가?
- [ ] OpenAI 응답이 `{"reply": "..."}` 형태인가?
- [ ] 적절한 HTTP 상태 코드를 사용하는가?
- [ ] Pydantic 모델로 요청/응답을 정의했는가?
- [ ] 에러 처리가 구현되었는가?
- [ ] 로깅이 적절히 구현되었는가?

### 테스트 시
- [ ] curl로 모든 엔드포인트를 테스트했는가?
- [ ] 잘못된 입력에 대한 에러 처리를 확인했는가?
- [ ] 응답 형식이 일관되는가?
- [ ] 성능이 적절한가?

### 배포 전
- [ ] API 문서가 업데이트되었는가?
- [ ] 보안 설정이 적절한가?
- [ ] 모니터링이 설정되었는가?
- [ ] 백업 및 복구 계획이 있는가?
