# at-thirty-rules 프로젝트 구조 가이드

## 📁 디렉토리 구조

```
pmsang/
├── main.py                    # FastAPI 앱 진입점
├── requirements.txt           # Python 의존성 목록
├── .env                      # 환경 변수 (보안상 .gitignore 포함)
├── .env.example              # 환경 변수 예시 파일
├── Procfile                  # Render 배포용
├── vercel.json               # Vercel 배포용
├── AT_THIRTY_RULES.md        # 프로젝트 규칙 문서
├── PROJECT_STRUCTURE.md      # 프로젝트 구조 가이드
├── README.md                 # 프로젝트 설명서
├── app/                      # 애플리케이션 메인 디렉토리
│   ├── __init__.py          # Python 패키지 초기화
│   ├── services/            # 비즈니스 로직 모듈
│   │   ├── __init__.py
│   │   ├── openai_service.py    # OpenAI API 서비스
│   │   ├── fortune_service.py   # 사주 관련 서비스
│   │   └── chat_service.py      # 채팅 관련 서비스
│   └── static/              # 정적 파일 서빙
│       ├── html/            # HTML 파일
│       │   ├── index.html       # 메인 페이지
│       │   ├── chat.html        # 채팅 페이지
│       │   └── fortune.html     # 사주 페이지
│       ├── css/             # CSS 스타일시트
│       │   ├── main.css         # 메인 스타일
│       │   ├── chat.css         # 채팅 스타일
│       │   └── fortune.css      # 사주 스타일
│       └── js/              # JavaScript 파일
│           ├── main.js          # 메인 스크립트
│           ├── chat.js          # 채팅 기능
│           └── fortune.js       # 사주 기능
├── tests/                   # 테스트 파일
│   ├── __init__.py
│   ├── test_api.py          # API 테스트
│   └── test_services.py     # 서비스 테스트
└── docs/                    # 문서화
    ├── api_spec.md          # API 명세서
    └── deployment.md        # 배포 가이드
```

## 📋 파일별 역할 설명

### 루트 디렉토리 파일

#### `main.py`
- **역할**: FastAPI 애플리케이션의 진입점
- **내용**: 
  - FastAPI 앱 초기화
  - 정적 파일 마운트 설정
  - 기본 라우트 정의
  - 환경 변수 로드
- **규칙**: 
  - 비즈니스 로직은 `app/services/`에 위임
  - API 라우트는 `/api/*` 경로로 통일

#### `requirements.txt`
- **역할**: Python 패키지 의존성 관리
- **포함 패키지**:
  - fastapi: 웹 프레임워크
  - uvicorn: ASGI 서버
  - python-dotenv: 환경 변수 관리
  - openai: OpenAI API 클라이언트
  - python-multipart: 파일 업로드 지원

#### `.env` / `.env.example`
- **역할**: 환경 변수 관리
- **포함 변수**:
  - `OPENAI_API_KEY`: OpenAI API 키
  - `HOST`: 서버 호스트
  - `PORT`: 서버 포트
  - `DEBUG`: 디버그 모드

### `app/` 디렉토리

#### `app/services/`
- **역할**: 비즈니스 로직 모듈
- **구성**:
  - `openai_service.py`: OpenAI API 호출 로직
  - `fortune_service.py`: 사주 계산 및 조회 로직
  - `chat_service.py`: 채팅 처리 로직

#### `app/static/`
- **역할**: 정적 파일 서빙
- **구성**:
  - `html/`: HTML 템플릿 파일
  - `css/`: 스타일시트 파일
  - `js/`: JavaScript 파일

### `tests/` 디렉토리
- **역할**: 테스트 코드 관리
- **구성**:
  - `test_api.py`: API 엔드포인트 테스트
  - `test_services.py`: 서비스 로직 테스트

## 🔧 구조 설계 원칙

### 1. 관심사 분리 (Separation of Concerns)
```
main.py          → 앱 설정 및 라우팅
app/services/    → 비즈니스 로직
app/static/      → 프론트엔드 리소스
tests/           → 테스트 코드
```

### 2. 모듈화 (Modularity)
- 각 서비스는 독립적인 모듈로 구성
- 공통 기능은 유틸리티 모듈로 분리
- 테스트는 기능별로 분리

### 3. 확장성 (Scalability)
- 새로운 기능 추가 시 기존 구조 유지
- API 버전 관리 준비
- 마이크로서비스 전환 가능한 구조

## 📝 파일 생성 규칙

### Python 파일
```python
# 파일 상단에 모듈 설명
"""
모듈명: openai_service.py
역할: OpenAI API 호출 관련 서비스
작성자: 개발자명
작성일: 2024-01-XX
"""

# 필요한 import 문
import os
from typing import Dict, Any
from fastapi import HTTPException

# 클래스 및 함수 정의
class OpenAIService:
    """OpenAI API 서비스 클래스"""
    pass
```

### HTML 파일
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>페이지 제목 - at-thirty-rules</title>
    <link rel="stylesheet" href="/static/css/main.css">
</head>
<body>
    <!-- 페이지 내용 -->
    <script src="/static/js/main.js"></script>
</body>
</html>
```

### CSS 파일
```css
/* 파일명: main.css */
/* 역할: 메인 스타일시트 */

/* CSS 변수 정의 */
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
}

/* 기본 스타일 */
body {
    font-family: 'Noto Sans KR', sans-serif;
    margin: 0;
    padding: 0;
}
```

### JavaScript 파일
```javascript
// 파일명: main.js
// 역할: 메인 JavaScript 로직

// 전역 변수
const API_BASE_URL = '/api';

// 유틸리티 함수
function formatDate(date) {
    // 날짜 포맷팅 로직
}

// 메인 함수
document.addEventListener('DOMContentLoaded', function() {
    // 초기화 로직
});
```

## 🚀 배포 구조

### Render 배포
```
Procfile: web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Vercel 배포
```json
{
  "version": 2,
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

## 📋 체크리스트

### 프로젝트 시작 시
- [ ] 디렉토리 구조 생성
- [ ] `__init__.py` 파일 생성
- [ ] `requirements.txt` 작성
- [ ] `.env.example` 생성
- [ ] 기본 HTML/CSS/JS 파일 생성

### 개발 중
- [ ] 새로운 기능은 적절한 모듈에 추가
- [ ] 정적 파일은 올바른 폴더에 배치
- [ ] 테스트 코드는 `tests/` 폴더에 작성
- [ ] 문서는 `docs/` 폴더에 업데이트

### 배포 전
- [ ] 모든 의존성이 `requirements.txt`에 포함
- [ ] 환경 변수 설정 확인
- [ ] 정적 파일 경로 확인
- [ ] API 엔드포인트 테스트
