// 파일명: chat.js
// 역할: 채팅 기능 JavaScript 로직

// API 기본 URL
const API_BASE = 'http://localhost:8000';

// 각 모델별 엔드포인트
const endpoints = {
    'gpt-35-turbo': '/chat/gpt-3.5-turbo',
    'gpt-4o': '/chat/gpt-4o',
    'gpt-4o-mini': '/chat/gpt-4o-mini',
    'gpt-4-turbo': '/chat/gpt-4-turbo'
};

// 폼 제출 이벤트 리스너 등록
Object.keys(endpoints).forEach(model => {
    const form = document.getElementById(`form-${model}`);
    const messageInput = document.getElementById(`message-${model}`);
    const button = document.getElementById(`btn-${model}`);
    const responseDiv = document.getElementById(`response-${model}`);
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const message = messageInput.value.trim();
        if (!message) return;
        
        // 로딩 상태
        button.disabled = true;
        button.textContent = '전송 중...';
        responseDiv.style.display = 'block';
        responseDiv.className = 'response loading';
        responseDiv.innerHTML = '🤔 AI가 답변을 생성하고 있습니다...';
        
        try {
            const response = await fetch(`${API_BASE}${endpoints[model]}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                responseDiv.className = 'response success';
                responseDiv.innerHTML = `
                    <strong>✅ ${data.model} 응답:</strong><br>
                    ${data.response}
                `;
            } else {
                responseDiv.className = 'response error';
                responseDiv.innerHTML = `
                    <strong>❌ 오류 발생:</strong><br>
                    ${data.error}
                `;
            }
        } catch (error) {
            responseDiv.className = 'response error';
            responseDiv.innerHTML = `
                <strong>❌ 네트워크 오류:</strong><br>
                ${error.message}
            `;
        } finally {
            button.disabled = false;
            button.textContent = `GPT-${model.replace('-', ' ').toUpperCase()}로 전송`;
        }
    });
});

// 각 폼이 독립적으로 작동하도록 설정
// 복사 기능 제거 - 각 폼이 독립적으로 작동
