# at-thirty-rules 프로젝트 전용 규칙

## 📋 프로젝트 개요
- **프로젝트명**: at-thirty-rules
- **목적**: 사주 검색 및 채팅 서비스
- **개발 기간**: 2024년

## 🛠 기술 스택

### Backend
- **언어**: Python 3.11
- **프레임워크**: FastAPI
- **서버**: Uvicorn
- **API**: OpenAI API (채팅 및 사주 검색)

### Frontend
- **언어**: HTML5, CSS3, Vanilla JavaScript
- **프레임워크**: 프레임워크 없음 (순수 웹 기술)

## 📁 프로젝트 구조 원칙

```
pmsang/
├── main.py                 # 앱 진입점
├── requirements.txt        # Python 의존성
├── .env                   # 환경 변수 (보안상 .gitignore에 포함)
├── app/
│   ├── services/          # 비즈니스 로직 모듈
│   │   ├── __init__.py
│   │   ├── openai_service.py
│   │   └── fortune_service.py
│   └── static/            # 정적 파일 서빙
│       ├── html/
│       ├── css/
│       └── js/
└── tests/                 # 테스트 파일
    └── test_api.py
```

### 구조 규칙
1. **main.py**: FastAPI 앱의 진입점으로만 사용
2. **app/services/**: 모든 비즈니스 로직을 모듈화하여 저장
3. **app/static/**: HTML, CSS, JS 파일을 폴더별로 정리
4. **모든 API**: `/api/*` 경로로 통일
5. **환경 변수**: `.env` 파일에서만 관리

## 🎨 코딩 스타일 가이드

### Python 코딩 규칙
```python
# 함수명: snake_case
def get_user_fortune(birth_date: str) -> dict:
    """
    사용자의 사주를 조회하는 함수
    
    Args:
        birth_date (str): 생년월일 (YYYY-MM-DD 형식)
    
    Returns:
        dict: 사주 정보가 담긴 딕셔너리
    """
    # 주석은 한국어로 작성
    pass

# 클래스명: PascalCase
class FortuneService:
    """사주 서비스 클래스"""
    pass

# 변수명: snake_case
user_name = "홍길동"
api_response = {"reply": "안녕하세요"}
```

### JavaScript 코딩 규칙
```javascript
// 함수명: camelCase
function getUserFortune(birthDate) {
    // 주석은 한국어로 작성
    // API 호출 로직
}

// 변수명: camelCase
const userName = "홍길동";
const apiResponse = { reply: "안녕하세요" };
```

### HTML/CSS 규칙
```html
<!-- 클래스명: kebab-case -->
<div class="fortune-container">
    <h1 class="main-title">사주 검색</h1>
</div>
```

```css
/* 클래스명: kebab-case */
.fortune-container {
    /* CSS 속성은 camelCase */
    backgroundColor: #f0f0f0;
}
```

## 🔧 API 설계 규칙

### API 엔드포인트 규칙
- **모든 API**: `/api/*` 경로로 시작
- **HTTP 메서드**: RESTful 원칙 준수
- **응답 형식**: 모든 OpenAI 응답은 `{"reply": "..."}` 형태로 통일

### API 예시
```python
@app.post("/api/chat")
async def chat_with_ai(message: str):
    """
    AI와 채팅하는 API
    
    Args:
        message (str): 사용자 메시지
    
    Returns:
        dict: {"reply": "AI 응답"}
    """
    try:
        response = await openai_service.get_chat_response(message)
        return {"reply": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/fortune")
async def get_fortune(birth_date: str):
    """
    사주를 조회하는 API
    
    Args:
        birth_date (str): 생년월일
    
    Returns:
        dict: {"reply": "사주 결과"}
    """
    try:
        fortune = await fortune_service.get_fortune(birth_date)
        return {"reply": fortune}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## 🔐 보안 규칙

### 환경 변수 관리
```python
# ❌ 잘못된 방법 - 코드에 직접 키 작성
openai_api_key = "sk-1234567890abcdef"

# ✅ 올바른 방법 - .env 파일에서 로드
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
```

### .env 파일 예시
```env
# OpenAI API 설정
OPENAI_API_KEY=your_openai_api_key_here

# 서버 설정
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

## 📝 문서화 규칙

### 함수 문서화
```python
def calculate_fortune_score(birth_date: str, name: str) -> int:
    """
    생년월일과 이름을 기반으로 사주 점수를 계산
    
    Args:
        birth_date (str): 생년월일 (YYYY-MM-DD)
        name (str): 사용자 이름
    
    Returns:
        int: 사주 점수 (0-100)
    
    Raises:
        ValueError: 잘못된 날짜 형식일 때
    """
    pass
```

### 주석 작성 규칙
```python
# FastAPI 앱 초기화
app = FastAPI(title="at-thirty-rules")

# OpenAI API 키 검증
if not openai_api_key:
    raise HTTPException(status_code=500, detail="API 키가 없습니다")

# 사용자 입력 검증
if not birth_date or len(birth_date) != 10:
    raise ValueError("올바른 날짜 형식이 아닙니다")
```

## 🧪 테스트 규칙

### 로컬 테스트
```bash
# 개발 서버 실행
uvicorn main:app --reload

# 서버 실행 (포트 지정)
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### API 테스트 (curl)
```bash
# 헬스 체크
curl -X GET "http://localhost:8000/api/health"

# 채팅 API 테스트
curl -X POST "http://localhost:8000/api/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "안녕하세요"}'

# 사주 API 테스트
curl -X POST "http://localhost:8000/api/fortune" \
     -H "Content-Type: application/json" \
     -d '{"birth_date": "1990-01-01"}'
```

## 🚀 배포 규칙

### Render 배포
1. **requirements.txt** 파일 준비
2. **Procfile** 생성: `web: uvicorn main:app --host 0.0.0.0 --port $PORT`
3. 환경 변수 설정 (OPENAI_API_KEY)

### Vercel 배포
1. **vercel.json** 설정 파일 생성
2. **api/** 폴더에 Python 함수 배치
3. 환경 변수 설정

## 📋 체크리스트

### 개발 시작 전
- [ ] Python 3.11 설치 확인
- [ ] .env 파일 생성 및 API 키 설정
- [ ] requirements.txt 의존성 설치
- [ ] 프로젝트 구조 생성

### 코드 작성 시
- [ ] 모든 함수에 docstring 추가
- [ ] 변수명은 snake_case (Python) / camelCase (JS)
- [ ] 클래스명은 PascalCase
- [ ] 주석은 한국어로 작성
- [ ] API는 /api/* 경로로 통일
- [ ] OpenAI 응답은 {"reply": "..."} 형태로 반환

### 테스트 시
- [ ] uvicorn main:app --reload로 로컬 테스트
- [ ] curl로 API 엔드포인트 테스트
- [ ] 에러 핸들링 확인

### 배포 전
- [ ] README.md 업데이트
- [ ] 환경 변수 설정 확인
- [ ] API 명세서 작성
- [ ] 배포 방법 문서화

## 🔄 업데이트 이력
- **2024-01-XX**: 초기 규칙 생성
- **2024-01-XX**: API 설계 규칙 추가
- **2024-01-XX**: 보안 규칙 강화
