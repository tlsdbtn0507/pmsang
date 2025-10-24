#!/bin/bash

# pmsang 프로젝트 가상환경 설정 스크립트

echo "🚀 pmsang 프로젝트 가상환경 설정을 시작합니다..."

# 가상환경이 이미 존재하는지 확인
if [ -d "venv" ]; then
    echo "⚠️  가상환경이 이미 존재합니다. 기존 가상환경을 삭제하고 새로 생성합니다."
    rm -rf venv
fi

# Python 버전 확인
echo "📋 Python 버전 확인 중..."
python3 --version

# 가상환경 생성
echo "🔧 가상환경 생성 중..."
python3 -m venv venv

# 가상환경 활성화
echo "⚡ 가상환경 활성화 중..."
source venv/bin/activate

# pip 업그레이드
echo "📦 pip 업그레이드 중..."
pip install --upgrade pip

# 의존성 설치
echo "📚 의존성 설치 중..."
pip install -r requirements.txt

# .env 파일이 없으면 생성
if [ ! -f ".env" ]; then
    echo "🔑 .env 파일 생성 중..."
    cat > .env << EOF
# OpenAI API 설정
OPENAI_API_KEY=your_openai_api_key_here

# 서버 설정
HOST=0.0.0.0
PORT=8000
DEBUG=True
EOF
    echo "✅ .env 파일이 생성되었습니다. OPENAI_API_KEY를 설정해주세요."
fi

echo ""
echo "🎉 가상환경 설정이 완료되었습니다!"
echo ""
echo "📝 다음 단계:"
echo "1. 가상환경 활성화: source venv/bin/activate"
echo "2. .env 파일에서 OPENAI_API_KEY 설정"
echo "3. 서버 실행: python src/main.py"
echo ""
echo "💡 가상환경 비활성화: deactivate"
