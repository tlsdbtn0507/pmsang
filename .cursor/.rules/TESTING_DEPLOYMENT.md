# at-thirty-rules 테스트 및 배포 규칙

## 🧪 테스트 규칙

### 1. 로컬 테스트 환경 설정

#### 개발 서버 실행
```bash
# 의존성 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
# .env 파일에서 OPENAI_API_KEY 설정

# 개발 서버 실행
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### 서버 실행 옵션
```bash
# 기본 실행
uvicorn main:app --reload

# 포트 지정 실행
uvicorn main:app --reload --port 8080

# 호스트 지정 실행
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 로그 레벨 지정
uvicorn main:app --reload --log-level debug

# 워커 수 지정 (프로덕션)
uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000
```

### 2. API 테스트 방법

#### curl을 이용한 테스트
```bash
#!/bin/bash
# test_api.sh - API 테스트 스크립트

BASE_URL="http://localhost:8000"
echo "=== at-thirty-rules API 테스트 시작 ==="

# 1. 헬스 체크
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
       "user_id": "test_user_001"
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

# 4. 에러 케이스 테스트
echo "4. 에러 케이스 테스트"
curl -X POST "${BASE_URL}/api/fortune" \
     -H "Content-Type: application/json" \
     -d '{
       "birth_date": "invalid-date",
       "name": "홍길동"
     }' \
     -w "\nHTTP Status: %{http_code}\n\n"

echo "=== API 테스트 완료 ==="
```

#### Python 테스트 코드
```python
# tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestHealthAPI:
    """헬스 체크 API 테스트"""
    
    def test_health_check_success(self):
        """헬스 체크 성공 테스트"""
        response = client.get("/api/health")
        assert response.status_code == 200
        
        data = response.json()
        assert "reply" in data
        assert data["status"] == "healthy"
        assert "timestamp" in data

class TestChatAPI:
    """채팅 API 테스트"""
    
    def test_chat_success(self):
        """채팅 성공 테스트"""
        response = client.post("/api/chat", json={
            "message": "안녕하세요!",
            "user_id": "test_user"
        })
        assert response.status_code == 200
        
        data = response.json()
        assert "reply" in data
        assert "conversation_id" in data
        assert "timestamp" in data
    
    def test_chat_missing_message(self):
        """메시지 누락 테스트"""
        response = client.post("/api/chat", json={
            "user_id": "test_user"
        })
        assert response.status_code == 422  # Validation Error

class TestFortuneAPI:
    """사주 API 테스트"""
    
    def test_fortune_success(self):
        """사주 조회 성공 테스트"""
        response = client.post("/api/fortune", json={
            "birth_date": "1990-01-15",
            "name": "홍길동"
        })
        assert response.status_code == 200
        
        data = response.json()
        assert "reply" in data
        assert "fortune_data" in data
        assert "timestamp" in data
    
    def test_fortune_invalid_date(self):
        """잘못된 날짜 형식 테스트"""
        response = client.post("/api/fortune", json={
            "birth_date": "invalid-date",
            "name": "홍길동"
        })
        assert response.status_code == 400
        
        data = response.json()
        assert "오류가 발생했습니다" in data["reply"]
    
    def test_fortune_missing_birth_date(self):
        """생년월일 누락 테스트"""
        response = client.post("/api/fortune", json={
            "name": "홍길동"
        })
        assert response.status_code == 422  # Validation Error

# 테스트 실행
if __name__ == "__main__":
    pytest.main(["-v", "tests/test_api.py"])
```

### 3. 성능 테스트

#### 부하 테스트 (Apache Bench)
```bash
# 동시 10명, 총 1000회 요청
ab -n 1000 -c 10 http://localhost:8000/api/health

# POST 요청 테스트
ab -n 100 -c 5 -p fortune_data.json -T application/json http://localhost:8000/api/fortune
```

#### 부하 테스트 데이터 파일
```json
# fortune_data.json
{
    "birth_date": "1990-01-15",
    "name": "홍길동",
    "birth_time": "14:30",
    "gender": "male"
}
```

### 4. 테스트 자동화

#### pytest 설정 파일
```ini
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

#### GitHub Actions 워크플로우
```yaml
# .github/workflows/test.yml
name: Test

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python 3.11
      uses: actions/setup-python@v2
      with:
        python-version: 3.11
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ -v --cov=app --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v1
      with:
        file: ./coverage.xml
```

## 🚀 배포 규칙

### 1. Render 배포

#### Procfile 생성
```bash
# Procfile
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

#### Render 배포 설정
```yaml
# render.yaml
services:
  - type: web
    name: at-thirty-rules
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: OPENAI_API_KEY
        sync: false
      - key: HOST
        value: 0.0.0.0
      - key: PORT
        value: 8000
      - key: DEBUG
        value: false
```

#### 배포 단계
1. **GitHub 저장소 연결**
   ```bash
   # GitHub에 코드 푸시
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Render 서비스 생성**
   - Render 대시보드에서 "New Web Service" 선택
   - GitHub 저장소 연결
   - 빌드 명령어: `pip install -r requirements.txt`
   - 시작 명령어: `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **환경 변수 설정**
   - `OPENAI_API_KEY`: OpenAI API 키
   - `HOST`: 0.0.0.0
   - `PORT`: 8000
   - `DEBUG`: false

### 2. Vercel 배포

#### vercel.json 설정
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
  ],
  "env": {
    "OPENAI_API_KEY": "@openai_api_key"
  }
}
```

#### Vercel 배포 단계
1. **Vercel CLI 설치**
   ```bash
   npm i -g vercel
   ```

2. **프로젝트 배포**
   ```bash
   # Vercel 로그인
   vercel login
   
   # 프로젝트 배포
   vercel
   
   # 프로덕션 배포
   vercel --prod
   ```

3. **환경 변수 설정**
   ```bash
   # Vercel 대시보드에서 환경 변수 설정
   vercel env add OPENAI_API_KEY
   ```

### 3. Docker 배포

#### Dockerfile 생성
```dockerfile
# Dockerfile
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 포트 노출
EXPOSE 8000

# 환경 변수 설정
ENV PYTHONPATH=/app
ENV HOST=0.0.0.0
ENV PORT=8000

# 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Docker 배포 명령어
```bash
# Docker 이미지 빌드
docker build -t at-thirty-rules .

# Docker 컨테이너 실행
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_api_key_here \
  at-thirty-rules

# Docker Compose 사용
docker-compose up -d
```

#### docker-compose.yml
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - HOST=0.0.0.0
      - PORT=8000
      - DEBUG=false
    volumes:
      - ./app/static:/app/app/static
    restart: unless-stopped
```

### 4. 배포 전 체크리스트

#### 코드 품질 검사
```bash
# 코드 포맷팅 검사
black --check .

# 린팅 검사
flake8 .

# 타입 검사
mypy .

# 보안 검사
bandit -r .
```

#### 배포 준비
- [ ] 모든 테스트 통과
- [ ] 환경 변수 설정 완료
- [ ] 데이터베이스 마이그레이션 (필요시)
- [ ] 정적 파일 최적화
- [ ] 로그 설정 확인
- [ ] 모니터링 설정
- [ ] 백업 계획 수립

### 5. 모니터링 및 로깅

#### 로깅 설정
```python
# main.py에 추가
import logging
from logging.handlers import RotatingFileHandler

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('logs/app.log', maxBytes=10000000, backupCount=5),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

#### 헬스 체크 엔드포인트
```python
@app.get("/api/health/detailed")
async def detailed_health_check():
    """상세 헬스 체크"""
    health_status = {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "uptime": get_uptime(),
        "memory_usage": get_memory_usage(),
        "openai_status": await check_openai_status()
    }
    
    return {"reply": "상세 상태 정보", "details": health_status}
```

## 📋 배포 후 검증

### 1. 배포 검증 체크리스트
- [ ] 서비스가 정상적으로 시작되는가?
- [ ] 모든 API 엔드포인트가 응답하는가?
- [ ] 환경 변수가 올바르게 설정되었는가?
- [ ] 로그가 정상적으로 기록되는가?
- [ ] 에러 처리가 작동하는가?
- [ ] 성능이 예상 범위 내인가?

### 2. 모니터링 설정
```python
# 모니터링 미들웨어
@app.middleware("http")
async def monitoring_middleware(request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    
    # 메트릭 수집
    logger.info(f"Request: {request.method} {request.url} - "
                f"Status: {response.status_code} - "
                f"Time: {process_time:.3f}s")
    
    return response
```

### 3. 롤백 계획
```bash
# 이전 버전으로 롤백
git checkout previous-version
git push origin main

# 또는 Docker 태그를 사용한 롤백
docker run -p 8000:8000 at-thirty-rules:previous-version
```

## 🔄 지속적 배포 (CI/CD)

### GitHub Actions 워크플로우
```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy to Render
      uses: render/deploy-action@v1
      with:
        service-id: ${{ secrets.RENDER_SERVICE_ID }}
        api-key: ${{ secrets.RENDER_API_KEY }}
    
    - name: Deploy to Vercel
      uses: amondnet/vercel-action@v20
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.ORG_ID }}
        vercel-project-id: ${{ secrets.PROJECT_ID }}
        working-directory: ./
```

이제 at-thirty-rules 프로젝트의 모든 규칙이 완성되었습니다! 🎉
