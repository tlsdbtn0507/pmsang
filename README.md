# PMSANG - 오행 기반 PM 성향 분석 서비스

PMSANG은 사주(四柱) 기반 오행 분석을 통해 사용자의 PM 성향을 파악하고, 맞춤형 에듀테크 PM 교육과정을 안내하는 서비스입니다.

## 프로젝트 구조

```
pmsang/
├── src/                    # Python 소스 코드
│   ├── __init__.py
│   ├── main.py            # FastAPI 메인 애플리케이션
│   └── saju_calculator.py # 오행 계산기
├── scripts/               # 실행 스크립트
│   ├── setup_venv.sh     # 가상환경 설정
│   ├── activate_venv.sh  # 가상환경 활성화
│   └── run.sh            # 서버 실행
├── app/                   # 웹 애플리케이션
│   ├── static/           # 정적 파일
│   │   ├── chat.html     # 웹 인터페이스
│   │   ├── css/          # 스타일시트
│   │   └── js/           # JavaScript
│   └── __init__.py
├── .cursor/               # 프로젝트 규칙
│   └── .rules/
│       └── PROJECT_RULES.md
├── venv/                  # 가상환경
├── data/                  # 데이터 파일
├── requirements.txt       # Python 의존성
└── README.md             # 프로젝트 문서
```

## 기능

### 🎯 현재 단계 (1단계): 오행 기반 PM 성향 분석
- 생년월일시 입력을 통한 오행 계산
- 5가지 오행별 PM 성향 분석 (🌳 리더형, 🔥 드라이버형, 🪨 안정형, ⚙️ 분석형, 💧 사용자형)
- 오행에 맞는 PM 성향 스크립트 제공
- 웹 인터페이스를 통한 직관적인 사용자 경험

### 🚀 향후 단계 (2-3단계): 에듀테크 PM 교육 연계
- PM 성향 기반 설문 테스트
- 맞춤형 에듀테크 PM 교육과정 안내
- 스크립트 기반 상담 서비스

## 설치 및 실행

1. 가상환경 설정:
```bash
./scripts/setup_venv.sh
```

2. 가상환경 활성화:
```bash
./scripts/activate_venv.sh
```

3. 서버 실행:
```bash
./scripts/run.sh
```

4. 브라우저에서 접속:
```
http://localhost:8001/chat
```

## API

### POST /saju/analyze

생년월일시를 입력받아 오행과 PM 성향을 분석합니다.

**요청:**
```json
{
    "year": 1997,
    "month": 5,
    "day": 7,
    "hour": 21,
    "minute": 0
}
```

**응답:**
```json
{
    "status": "success",
    "birth_date": "1997년 5월 7일 21시 0분",
    "five_element": "나무",
    "message": "당신의 오행은 '나무'입니다.",
    "pm_script": {
        "title": "🌳 목(木) — 성장과 확장의 리더형 PM",
        "description": "당신은 목(木) 오행의 PM입니다. 성장과 확장을 추구하는 리더형 PM으로, 새로운 아이디어를 발굴하고 팀을 이끌어가는 능력이 뛰어납니다."
    }
}
```

## PM 성향 유형

- 🌳 **목(木) - 리더형 PM**: 성장과 확장을 추구하는 리더형
- 🔥 **화(火) - 드라이버형 PM**: 추진력과 실행력이 뛰어난 드라이버형  
- 🪨 **토(土) - 안정형 PM**: 균형과 안정을 중시하는 관리형
- ⚙️ **금(金) - 분석형 PM**: 논리와 데이터에 강한 분석형
- 💧 **수(水) - 사용자형 PM**: 공감과 소통이 뛰어난 사용자형