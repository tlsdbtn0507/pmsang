#!/bin/bash

# pmsang 프로젝트 실행 스크립트

echo "🚀 pmsang 프로젝트를 시작합니다..."

# 가상환경이 존재하는지 확인
if [ ! -d "venv" ]; then
    echo "❌ 가상환경이 존재하지 않습니다. 먼저 setup_venv.sh를 실행해주세요."
    echo "   실행 명령: ./setup_venv.sh"
    exit 1
fi

# 가상환경 활성화
echo "⚡ 가상환경 활성화 중..."
source venv/bin/activate

# .env 파일 존재 확인
if [ ! -f ".env" ]; then
    echo "❌ .env 파일이 존재하지 않습니다. 먼저 setup_venv.sh를 실행해주세요."
    exit 1
fi

# 서버 실행
echo "🌐 서버를 시작합니다..."
echo "   - 웹 인터페이스: http://localhost:8001"
echo "   - API 문서: http://localhost:8001/docs"
echo "   - 서버 중지: Ctrl+C"
echo ""

PORT=8001 python src/main.py
