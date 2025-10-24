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