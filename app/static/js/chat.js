// 오행 계산기 JavaScript

// API 기본 URL
const API_BASE = 'http://localhost:8000';

// DOM이 완전히 로드된 후 실행
document.addEventListener('DOMContentLoaded', function() {
    // 오행 계산 폼 이벤트 리스너
    document.getElementById('form-saju-analysis').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const birthDate = document.getElementById('birthDate').value;
    const birthTime = document.getElementById('birthTime').value;
    const gender = document.getElementById('gender').value;
    const birthPlace = document.getElementById('birthPlace').value;
    const button = document.getElementById('btn-saju-analysis');
    const responseDiv = document.getElementById('response-saju-analysis');
    
    // 로딩 상태
    button.disabled = true;
    button.textContent = '계산 중...';
    responseDiv.style.display = 'block';
    responseDiv.className = 'response loading';
    responseDiv.innerHTML = '🔮 오행을 계산하고 있습니다...';
    
    try {
        const response = await fetch(`${API_BASE}/saju/analyze`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                birth_date: birthDate,
                birth_time: birthTime,
                gender: gender,
                birth_place: birthPlace
            })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            responseDiv.className = 'response success';
            
            responseDiv.innerHTML = `
                <div style="text-align: center; padding: 20px;">
                    <h3>🎉 당신의 오행 결과</h3>
                    <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin: 20px 0;">
                        <div style="font-size: 18px; margin-bottom: 10px;">
                            <strong>출생일:</strong> ${data.birth_date}
                        </div>
                        <div style="font-size: 16px; margin-bottom: 10px;">
                            <strong>성별:</strong> ${data.gender} | <strong>출생지역:</strong> ${data.birth_place}
                        </div>
                        <div style="font-size: 24px; font-weight: bold; color: #ffd700; margin: 20px 0;">
                            오행: ${data.five_element}
                        </div>
                        <div style="padding: 15px; background: rgba(255,255,255,0.05); border-radius: 8px; margin: 15px 0;">
                            ${data.message.split('\n\n').map(line => 
                                line.trim() ? `<p style="font-size: 16px; color: #ccc; line-height: 1.8; margin: 8px 0; text-align: left; display: block;">${line}</p>` : ''
                            ).join('')}
                        </div>
                    </div>
                </div>
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
        button.textContent = '오행 확인하기';
    }
    });
});