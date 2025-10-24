// 오행 계산기 JavaScript

// API 기본 URL - 환경변수에서 가져오거나 기본값 사용
const API_BASE = window.API_BASE_URL || window.location.origin;

// DOM이 완전히 로드된 후 실행
document.addEventListener('DOMContentLoaded', function() {
    // 오행 계산 폼 이벤트 리스너
    document.getElementById('form-saju-analysis').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const birthDate = document.getElementById('birthDate').value;
    const birthTime = document.getElementById('birthTime').value;
    const gender = document.getElementById('gender').value;
    const birthPlace = document.getElementById('birthPlace').value;
    
    // 필수 필드 검증
    if (!birthDate || !birthTime || !gender || !birthPlace) {
        alert('모든 필드를 입력해주세요.');
        return;
    }
    
    const params = new URLSearchParams({
        birth_date: birthDate,
        birth_time: birthTime,
        gender: gender,
        birth_place: birthPlace
    });
    
    // 상세 분석 페이지로 이동
    window.location.href = `/saju/analysis?${params.toString()}`;

    });
});