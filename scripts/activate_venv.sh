#!/bin/bash

# pmsang 프로젝트 가상환경 활성화 스크립트

echo "⚡ pmsang 가상환경을 활성화합니다..."

# 가상환경이 존재하는지 확인
if [ ! -d "venv" ]; then
    echo "❌ 가상환경이 존재하지 않습니다. 먼저 setup_venv.sh를 실행해주세요."
    echo "   실행 명령: ./setup_venv.sh"
    exit 1
fi

# 가상환경 활성화
source venv/bin/activate

echo "✅ 가상환경이 활성화되었습니다!"
echo ""
echo "📝 사용 가능한 명령어:"
echo "   - 서버 실행: python src/main.py"
echo "   - 의존성 설치: pip install -r requirements.txt"
echo "   - 가상환경 비활성화: deactivate"
echo ""
echo "💡 현재 가상환경에서 작업을 진행하세요."
