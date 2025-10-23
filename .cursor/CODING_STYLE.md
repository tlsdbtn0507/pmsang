# at-thirty-rules 코딩 스타일 가이드

## 🐍 Python 코딩 스타일

### 1. 명명 규칙 (Naming Conventions)

#### 변수 및 함수명: `snake_case`
```python
# ✅ 올바른 예시
user_name = "홍길동"
birth_date = "1990-01-01"
api_response = {"reply": "안녕하세요"}

def get_user_fortune(birth_date: str) -> dict:
    """사용자 사주 조회 함수"""
    pass

def calculate_fortune_score(name: str, birth_date: str) -> int:
    """사주 점수 계산 함수"""
    pass
```

#### 클래스명: `PascalCase`
```python
# ✅ 올바른 예시
class FortuneService:
    """사주 서비스 클래스"""
    pass

class OpenAIService:
    """OpenAI API 서비스 클래스"""
    pass

class ChatHandler:
    """채팅 처리 클래스"""
    pass
```

#### 상수: `UPPER_SNAKE_CASE`
```python
# ✅ 올바른 예시
MAX_FORTUNE_SCORE = 100
DEFAULT_API_TIMEOUT = 30
OPENAI_MODEL = "gpt-3.5-turbo"
```

### 2. 함수 작성 규칙

#### 함수 시그니처
```python
def function_name(param1: type, param2: type = default_value) -> return_type:
    """
    함수 설명 (한 줄 요약)
    
    Args:
        param1 (type): 매개변수1 설명
        param2 (type, optional): 매개변수2 설명. Defaults to default_value.
    
    Returns:
        return_type: 반환값 설명
    
    Raises:
        ValueError: 발생 조건 설명
        HTTPException: 발생 조건 설명
    
    Example:
        >>> result = function_name("test", 123)
        >>> print(result)
        {"status": "success"}
    """
    pass
```

#### 실제 예시
```python
def get_fortune_by_birth_date(birth_date: str, name: str = None) -> dict:
    """
    생년월일을 기반으로 사주를 조회하는 함수
    
    Args:
        birth_date (str): 생년월일 (YYYY-MM-DD 형식)
        name (str, optional): 사용자 이름. Defaults to None.
    
    Returns:
        dict: 사주 정보가 담긴 딕셔너리
            - fortune_type: 사주 유형
            - score: 사주 점수
            - description: 사주 설명
    
    Raises:
        ValueError: 잘못된 날짜 형식일 때
        HTTPException: API 호출 실패 시
    
    Example:
        >>> fortune = get_fortune_by_birth_date("1990-01-01", "홍길동")
        >>> print(fortune["score"])
        85
    """
    # 입력 검증
    if not birth_date or len(birth_date) != 10:
        raise ValueError("올바른 날짜 형식이 아닙니다 (YYYY-MM-DD)")
    
    # 비즈니스 로직
    try:
        # 사주 계산 로직
        result = calculate_fortune_logic(birth_date, name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"사주 조회 실패: {str(e)}")
```

### 3. 클래스 작성 규칙

```python
class FortuneService:
    """
    사주 관련 서비스를 제공하는 클래스
    
    Attributes:
        openai_client: OpenAI API 클라이언트
        fortune_cache: 사주 결과 캐시
    """
    
    def __init__(self, api_key: str):
        """
        FortuneService 초기화
        
        Args:
            api_key (str): OpenAI API 키
        """
        self.openai_client = OpenAI(api_key=api_key)
        self.fortune_cache = {}
    
    def get_fortune(self, birth_date: str, name: str = None) -> dict:
        """
        사주를 조회하는 메서드
        
        Args:
            birth_date (str): 생년월일
            name (str, optional): 사용자 이름
        
        Returns:
            dict: 사주 결과
        """
        # 캐시 확인
        cache_key = f"{birth_date}_{name or 'unknown'}"
        if cache_key in self.fortune_cache:
            return self.fortune_cache[cache_key]
        
        # 사주 계산
        fortune_result = self._calculate_fortune(birth_date, name)
        
        # 캐시 저장
        self.fortune_cache[cache_key] = fortune_result
        
        return fortune_result
    
    def _calculate_fortune(self, birth_date: str, name: str) -> dict:
        """
        실제 사주 계산 로직 (private 메서드)
        
        Args:
            birth_date (str): 생년월일
            name (str): 사용자 이름
        
        Returns:
            dict: 계산된 사주 결과
        """
        # 사주 계산 로직
        pass
```

### 4. 주석 작성 규칙

#### 인라인 주석
```python
# OpenAI API 키 검증
if not openai_api_key:
    raise HTTPException(status_code=500, detail="API 키가 설정되지 않았습니다")

# 사용자 입력 검증
if not birth_date or len(birth_date) != 10:
    raise ValueError("올바른 날짜 형식이 아닙니다")

# 사주 점수 계산 (0-100 범위)
fortune_score = calculate_score(birth_date, name)

# API 응답 형식 통일
response = {"reply": fortune_result}
```

#### 블록 주석
```python
"""
사주 계산 메인 로직
1. 생년월일을 사주 요소로 변환
2. 각 요소별 점수 계산
3. 종합 점수 산출
4. 결과 포맷팅
"""
def calculate_fortune_score(birth_date: str, name: str) -> int:
    # 생년월일 파싱
    year, month, day = birth_date.split('-')
    
    # 사주 요소 계산
    # ... 계산 로직 ...
    
    return total_score
```

## 🌐 JavaScript 코딩 스타일

### 1. 명명 규칙

#### 변수 및 함수명: `camelCase`
```javascript
// ✅ 올바른 예시
const userName = "홍길동";
const birthDate = "1990-01-01";
const apiResponse = { reply: "안녕하세요" };

function getUserFortune(birthDate) {
    // 사주 조회 함수
}

function calculateFortuneScore(name, birthDate) {
    // 사주 점수 계산 함수
}
```

#### 클래스명: `PascalCase`
```javascript
// ✅ 올바른 예시
class FortuneService {
    constructor(apiKey) {
        this.apiKey = apiKey;
    }
}

class ChatHandler {
    constructor() {
        this.messageHistory = [];
    }
}
```

#### 상수: `UPPER_SNAKE_CASE`
```javascript
// ✅ 올바른 예시
const API_BASE_URL = '/api';
const MAX_FORTUNE_SCORE = 100;
const DEFAULT_TIMEOUT = 30000;
```

### 2. 함수 작성 규칙

```javascript
/**
 * 생년월일을 기반으로 사주를 조회하는 함수
 * @param {string} birthDate - 생년월일 (YYYY-MM-DD 형식)
 * @param {string} [name] - 사용자 이름 (선택사항)
 * @returns {Promise<Object>} 사주 정보 객체
 * @throws {Error} 잘못된 날짜 형식 또는 API 호출 실패 시
 * 
 * @example
 * const fortune = await getFortuneByBirthDate('1990-01-01', '홍길동');
 * console.log(fortune.score); // 85
 */
async function getFortuneByBirthDate(birthDate, name = null) {
    // 입력 검증
    if (!birthDate || birthDate.length !== 10) {
        throw new Error('올바른 날짜 형식이 아닙니다 (YYYY-MM-DD)');
    }
    
    try {
        // API 호출
        const response = await fetch(`${API_BASE_URL}/fortune`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                birth_date: birthDate,
                name: name
            })
        });
        
        if (!response.ok) {
            throw new Error(`API 호출 실패: ${response.status}`);
        }
        
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('사주 조회 실패:', error);
        throw error;
    }
}
```

### 3. 클래스 작성 규칙

```javascript
/**
 * 사주 관련 서비스를 제공하는 클래스
 */
class FortuneService {
    /**
     * FortuneService 초기화
     * @param {string} apiKey - OpenAI API 키
     */
    constructor(apiKey) {
        this.apiKey = apiKey;
        this.fortuneCache = new Map();
    }
    
    /**
     * 사주를 조회하는 메서드
     * @param {string} birthDate - 생년월일
     * @param {string} [name] - 사용자 이름
     * @returns {Promise<Object>} 사주 결과
     */
    async getFortune(birthDate, name = null) {
        // 캐시 확인
        const cacheKey = `${birthDate}_${name || 'unknown'}`;
        if (this.fortuneCache.has(cacheKey)) {
            return this.fortuneCache.get(cacheKey);
        }
        
        // 사주 계산
        const fortuneResult = await this._calculateFortune(birthDate, name);
        
        // 캐시 저장
        this.fortuneCache.set(cacheKey, fortuneResult);
        
        return fortuneResult;
    }
    
    /**
     * 실제 사주 계산 로직 (private 메서드)
     * @private
     * @param {string} birthDate - 생년월일
     * @param {string} name - 사용자 이름
     * @returns {Promise<Object>} 계산된 사주 결과
     */
    async _calculateFortune(birthDate, name) {
        // 사주 계산 로직
        // ...
    }
}
```

## 🎨 HTML/CSS 코딩 스타일

### 1. HTML 구조 규칙

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>페이지 제목 - at-thirty-rules</title>
    
    <!-- CSS 파일 로드 -->
    <link rel="stylesheet" href="/static/css/main.css">
    <link rel="stylesheet" href="/static/css/fortune.css">
    
    <!-- 메타 태그 -->
    <meta name="description" content="사주 검색 및 채팅 서비스">
    <meta name="keywords" content="사주, 운세, 채팅, AI">
</head>
<body>
    <!-- 메인 컨테이너 -->
    <div class="main-container">
        <!-- 헤더 -->
        <header class="main-header">
            <h1 class="main-title">at-thirty-rules</h1>
            <nav class="main-navigation">
                <ul class="nav-list">
                    <li class="nav-item">
                        <a href="/" class="nav-link">홈</a>
                    </li>
                    <li class="nav-item">
                        <a href="/fortune" class="nav-link">사주</a>
                    </li>
                    <li class="nav-item">
                        <a href="/chat" class="nav-link">채팅</a>
                    </li>
                </ul>
            </nav>
        </header>
        
        <!-- 메인 콘텐츠 -->
        <main class="main-content">
            <!-- 페이지별 콘텐츠 -->
        </main>
        
        <!-- 푸터 -->
        <footer class="main-footer">
            <p class="footer-text">&copy; 2024 at-thirty-rules. All rights reserved.</p>
        </footer>
    </div>
    
    <!-- JavaScript 파일 로드 -->
    <script src="/static/js/main.js"></script>
    <script src="/static/js/fortune.js"></script>
</body>
</html>
```

### 2. CSS 클래스 명명 규칙: `kebab-case`

```css
/* 파일명: main.css */
/* 역할: 메인 스타일시트 */

/* CSS 변수 정의 */
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --danger-color: #dc3545;
    --warning-color: #ffc107;
    --info-color: #17a2b8;
    
    --font-family-primary: 'Noto Sans KR', sans-serif;
    --font-size-base: 16px;
    --line-height-base: 1.5;
    
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 3rem;
}

/* 기본 스타일 */
body {
    font-family: var(--font-family-primary);
    font-size: var(--font-size-base);
    line-height: var(--line-height-base);
    margin: 0;
    padding: 0;
    background-color: #f8f9fa;
}

/* 메인 컨테이너 */
.main-container {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

/* 헤더 스타일 */
.main-header {
    background-color: var(--primary-color);
    color: white;
    padding: var(--spacing-md);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.main-title {
    margin: 0;
    font-size: 1.5rem;
    font-weight: 700;
}

/* 네비게이션 */
.main-navigation {
    margin-top: var(--spacing-sm);
}

.nav-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    gap: var(--spacing-lg);
}

.nav-item {
    margin: 0;
}

.nav-link {
    color: white;
    text-decoration: none;
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: 4px;
    transition: background-color 0.2s ease;
}

.nav-link:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

/* 메인 콘텐츠 */
.main-content {
    flex: 1;
    padding: var(--spacing-xl);
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
    box-sizing: border-box;
}

/* 푸터 */
.main-footer {
    background-color: #343a40;
    color: white;
    text-align: center;
    padding: var(--spacing-md);
    margin-top: auto;
}

.footer-text {
    margin: 0;
    font-size: 0.9rem;
}
```

### 3. 반응형 디자인 규칙

```css
/* 모바일 우선 접근법 */
.fortune-container {
    padding: var(--spacing-md);
    margin: var(--spacing-md) 0;
}

/* 태블릿 (768px 이상) */
@media (min-width: 768px) {
    .fortune-container {
        padding: var(--spacing-lg);
        margin: var(--spacing-lg) 0;
    }
}

/* 데스크톱 (1024px 이상) */
@media (min-width: 1024px) {
    .fortune-container {
        padding: var(--spacing-xl);
        margin: var(--spacing-xl) 0;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
}
```

## 🔧 공통 코딩 규칙

### 1. 들여쓰기
- **Python**: 4칸 공백
- **JavaScript**: 2칸 공백 또는 4칸 공백 (일관성 유지)
- **HTML**: 2칸 공백
- **CSS**: 2칸 공백

### 2. 줄 길이
- 최대 100자 (Python), 120자 (JavaScript)
- 긴 줄은 적절히 분리

### 3. 빈 줄 사용
```python
# 함수 간 빈 줄
def function1():
    pass


def function2():
    pass


# 클래스 내부 메서드 간 빈 줄
class MyClass:
    def method1(self):
        pass
    
    def method2(self):
        pass
```

### 4. 임포트 순서
```python
# 표준 라이브러리
import os
import sys
from typing import Dict, List

# 서드파티 라이브러리
from fastapi import FastAPI, HTTPException
from openai import OpenAI

# 로컬 모듈
from app.services.openai_service import OpenAIService
from app.services.fortune_service import FortuneService
```

## 📋 코드 리뷰 체크리스트

### Python
- [ ] 함수명이 `snake_case`인가?
- [ ] 클래스명이 `PascalCase`인가?
- [ ] 모든 함수에 docstring이 있는가?
- [ ] 타입 힌트가 적절히 사용되었는가?
- [ ] 예외 처리가 적절한가?
- [ ] 주석이 한국어로 작성되었는가?

### JavaScript
- [ ] 변수명이 `camelCase`인가?
- [ ] 함수에 JSDoc 주석이 있는가?
- [ ] async/await가 적절히 사용되었는가?
- [ ] 에러 처리가 구현되었는가?
- [ ] DOM 조작이 효율적인가?

### HTML/CSS
- [ ] 클래스명이 `kebab-case`인가?
- [ ] 시맨틱 HTML이 사용되었는가?
- [ ] 접근성이 고려되었는가?
- [ ] 반응형 디자인이 적용되었는가?
- [ ] CSS 변수가 적절히 사용되었는가?
