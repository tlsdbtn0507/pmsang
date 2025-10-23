# at-thirty-rules 프로젝트

## 📋 프로젝트 개요

**at-thirty-rules**는 Python 3.11 + FastAPI + OpenAI API를 활용한 사주 검색 및 채팅 서비스입니다.

### 🎯 주요 기능
- **AI 채팅**: OpenAI API를 통한 자연어 대화
- **사주 검색**: 생년월일 기반 사주 조회 및 해석
- **웹 인터페이스**: HTML/CSS/Vanilla JS 기반 사용자 인터페이스

### 🛠 기술 스택
- **Backend**: Python 3.11, FastAPI, Uvicorn
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI**: OpenAI API (GPT-3.5-turbo)
- **배포**: Render, Vercel, Docker

## 📁 프로젝트 구조

```
pmsang/
├── main.py                    # FastAPI 앱 진입점
├── requirements.txt           # Python 의존성
├── .env.example              # 환경 변수 예시
├── README.md                 # 프로젝트 설명서
├── .cursor/                  # 프로젝트 규칙 문서
│   ├── AT_THIRTY_RULES.md    # 프로젝트 규칙 문서
│   ├── PROJECT_STRUCTURE.md  # 프로젝트 구조 가이드
│   ├── CODING_STYLE.md       # 코딩 스타일 가이드
│   ├── API_DESIGN.md         # API 설계 규칙
│   └── TESTING_DEPLOYMENT.md # 테스트 및 배포 규칙
└── app/                      # 애플리케이션 코드
    ├── services/             # 비즈니스 로직
    └── static/               # 정적 파일
        ├── html/             # HTML 파일
        ├── css/              # CSS 파일
        └── js/               # JavaScript 파일
```

## 🚀 빠른 시작

### 1. 환경 설정
```bash
# 저장소 클론
git clone <repository-url>
cd pmsang

# Python 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. 환경 변수 설정
```bash
# .env 파일 생성
cp .env.example .env

# .env 파일 편집
OPENAI_API_KEY=your_openai_api_key_here
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

### 3. 서버 실행
```bash
# 개발 서버 실행
uvicorn main:app --reload

# 또는 Python으로 실행
python main.py
```

### 4. 서비스 확인
- **웹 인터페이스**: http://localhost:8000
- **API 문서**: http://localhost:8000/docs
- **헬스 체크**: http://localhost:8000/api/health

## 📚 API 사용법

### 기본 엔드포인트
- `GET /api/health` - 서비스 상태 확인
- `POST /api/chat` - AI 채팅
- `POST /api/fortune` - 사주 조회

### API 사용 예시

#### 채팅 API
```bash
curl -X POST "http://localhost:8000/api/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "안녕하세요! 오늘 운세가 어떤가요?",
       "user_id": "user123"
     }'
```

#### 사주 API
```bash
curl -X POST "http://localhost:8000/api/fortune" \
     -H "Content-Type: application/json" \
     -d '{
       "birth_date": "1990-01-15",
       "name": "홍길동",
       "birth_time": "14:30",
       "gender": "male"
     }'
```

## 🧪 테스트

### 로컬 테스트
```bash
# API 테스트 스크립트 실행
chmod +x test_api.sh
./test_api.sh

# Python 테스트 실행
pytest tests/ -v
```

### 테스트 커버리지
```bash
pytest tests/ --cov=app --cov-report=html
```

## 🚀 배포

### Render 배포
1. GitHub 저장소에 코드 푸시
2. Render에서 새 웹 서비스 생성
3. GitHub 저장소 연결
4. 환경 변수 설정 (OPENAI_API_KEY)
5. 배포 완료

### Vercel 배포
```bash
# Vercel CLI 설치
npm i -g vercel

# 배포
vercel --prod
```

### Docker 배포
```bash
# Docker 이미지 빌드
docker build -t at-thirty-rules .

# 컨테이너 실행
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_api_key \
  at-thirty-rules
```

## 📖 문서

### 프로젝트 규칙
- **[.cursor/AT_THIRTY_RULES.md](.cursor/AT_THIRTY_RULES.md)**: 프로젝트 전용 규칙
- **[.cursor/PROJECT_STRUCTURE.md](.cursor/PROJECT_STRUCTURE.md)**: 프로젝트 구조 가이드
- **[.cursor/CODING_STYLE.md](.cursor/CODING_STYLE.md)**: 코딩 스타일 가이드
- **[.cursor/API_DESIGN.md](.cursor/API_DESIGN.md)**: API 설계 규칙
- **[.cursor/TESTING_DEPLOYMENT.md](.cursor/TESTING_DEPLOYMENT.md)**: 테스트 및 배포 규칙

### 개발 가이드
1. **코딩 스타일**: Python은 snake_case, JavaScript는 camelCase 사용
2. **API 설계**: 모든 API는 `/api/*` 경로로 통일
3. **응답 형식**: OpenAI 응답은 `{"reply": "..."}` 형태로 반환
4. **문서화**: 모든 함수에 docstring 추가, 주석은 한국어로 작성

## 🔧 개발 환경 설정

### 필수 요구사항
- Python 3.11+
- OpenAI API 키
- Git

### 권장 도구
- VS Code 또는 PyCharm
- Postman (API 테스트)
- Docker (컨테이너화)

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 문의

프로젝트에 대한 문의사항이 있으시면 이슈를 생성해 주세요.

---

**at-thirty-rules** - AI 기반 사주 검색 및 채팅 서비스 🎯
