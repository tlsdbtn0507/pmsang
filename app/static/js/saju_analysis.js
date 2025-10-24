// 사주 분석 페이지 JavaScript
class SajuAnalysis {
    constructor() {
        this.fiveElementColors = {
            '나무': 'wood',
            '불': 'fire', 
            '흙': 'earth',
            '금': 'metal',
            '물': 'water'
        };
        
        this.fiveElementEmojis = {
            '나무': '🌳',
            '불': '🔥',
            '흙': '🪨', 
            '금': '⚙️',
            '물': '💧'
        };

        this.fiveElementNames = {
            '나무': '목(木)',
            '불': '화(火)',
            '흙': '토(土)',
            '금': '금(金)',
            '물': '수(水)'
        };

        this.elementColorClasses = {
            '나무': 'bg-green-50 border-green-200 text-green-700',
            '불': 'bg-red-50 border-red-200 text-red-700',
            '흙': 'bg-orange-50 border-orange-200 text-orange-700',
            '금': 'bg-yellow-50 border-yellow-200 text-yellow-700',
            '물': 'bg-blue-50 border-blue-200 text-blue-700'
        };
    }

    async loadAnalysisFromURL() {
        // URL 파라미터에서 생년월일시 정보 가져오기
        const urlParams = new URLSearchParams(window.location.search);
        const birthDate = urlParams.get('birth_date');
        const birthTime = urlParams.get('birth_time');
        const gender = urlParams.get('gender') || '남';
        const birthPlace = urlParams.get('birth_place') || '서울';

        if (birthDate && birthTime) {
            try {
                const response = await fetch('/saju/detailed', {
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
                    this.updateAnalysis(data);
                } else {
                    console.error('사주 분석 실패:', data.error);
                    this.showError(data.error);
                }
            } catch (error) {
                console.error('API 호출 실패:', error);
                this.showError('사주 분석을 불러오는데 실패했습니다.');
            }
        } else {
            // URL 파라미터가 없으면 예시 데이터 사용
            this.showExampleData();
        }
    }

    updateAnalysis(sajuData) {
        // 오행 분석 업데이트
        const fiveElement = sajuData.five_element;
        const dayStem = sajuData.day_stem;
        const dayBranch = sajuData.day_branch;
        const dayPillar = sajuData.day_pillar;

        // 오행 태그 업데이트
        const fiveElementTag = document.getElementById('five-element-tag');
        if (fiveElementTag) {
            fiveElementTag.textContent = this.fiveElementNames[fiveElement];
        }

        // 천간지지 태그 업데이트
        const stemBranchTag = document.getElementById('stem-branch-tag');
        if (stemBranchTag) {
            stemBranchTag.textContent = `${dayStem}${dayBranch}`;
        }

        // 일주 태그 업데이트
        const dayPillarTag = document.getElementById('day-pillar-tag');
        if (dayPillarTag) {
            dayPillarTag.textContent = dayPillar;
        }

        // 사주 차트 업데이트
        this.updateSajuChart(sajuData);

        // 성향 정보 업데이트
        if (sajuData.traits) {
            this.updateTraits(sajuData.traits);
        }

        // 분석 설명 업데이트
        this.updateAnalysisDescriptions(sajuData);

        // 팁 업데이트
        this.updateTip(fiveElement, dayBranch);
    }

    updateSajuChart(sajuData) {
        if (sajuData.four_pillars) {
            const pillars = sajuData.four_pillars;
            
            // 시주 업데이트
            this.updatePillarCell('hour', pillars.hour);
            // 일주 업데이트  
            this.updatePillarCell('day', pillars.day);
            // 월주 업데이트
            this.updatePillarCell('month', pillars.month);
            // 년주 업데이트
            this.updatePillarCell('year', pillars.year);
        }
    }
    
    updatePillarCell(type, pillarData) {
        // 천간 업데이트
        const stemCell = document.getElementById(`${type}-stem`);
        
        if (stemCell) {
            const stemText = stemCell.querySelector('.font-bold');
            const stemDetail = stemCell.querySelector('.text-xs');
            
            if (stemText) stemText.textContent = pillarData.stem;
            if (stemDetail) stemDetail.textContent = pillarData.stem_hanja;
            
            // 오행별 색상 적용
            const element = this.getFiveElementFromStem(pillarData.stem);
            const colorClass = this.elementColorClasses[element];
            if (colorClass) {
                stemCell.className = `border rounded-md p-2 ${colorClass}`;
            }
        }
        
        // 십성 업데이트
        const tenGodCell = document.getElementById(`${type}-ten-god`);
        if (tenGodCell) {
            const tenGodText = tenGodCell.querySelector('.font-bold');
            const tenGodDetail = tenGodCell.querySelector('.text-xs');
            
            if (tenGodText) tenGodText.textContent = pillarData.ten_god;
            if (tenGodDetail) tenGodDetail.textContent = '';
        }
        
        // 지지 업데이트
        const branchCell = document.getElementById(`${type}-branch`);
        if (branchCell) {
            const branchText = branchCell.querySelector('.font-bold');
            const branchDetail = branchCell.querySelector('.text-xs');
            
            if (branchText) branchText.textContent = pillarData.branch;
            if (branchDetail) branchDetail.textContent = pillarData.branch_hanja;
            
            // 오행별 색상 적용
            const element = this.getFiveElementFromBranch(pillarData.branch);
            const colorClass = this.elementColorClasses[element];
            if (colorClass) {
                branchCell.className = `border rounded-md p-2 ${colorClass}`;
            }
        }
        
        // 지지 십성 업데이트
        const branchTenGodCell = document.getElementById(`${type}-branch-ten-god`);
        if (branchTenGodCell) {
            const branchTenGodText = branchTenGodCell.querySelector('.font-bold');
            const branchTenGodDetail = branchTenGodCell.querySelector('.text-xs');
            
            if (branchTenGodText) branchTenGodText.textContent = pillarData.branch_ten_god || '-';
            if (branchTenGodDetail) branchTenGodDetail.textContent = '';
        }
    }
    
    getFiveElementFromStem(stem) {
        const elementMap = {
            '갑': '나무', '을': '나무', '병': '불', '정': '불', '무': '흙', '기': '흙',
            '경': '금', '신': '금', '임': '물', '계': '물'
        };
        return elementMap[stem] || '';
    }
    
    getFiveElementFromBranch(branch) {
        const elementMap = {
            '자': '물', '축': '흙', '인': '나무', '묘': '나무', '진': '흙', '사': '불',
            '오': '불', '미': '흙', '신': '금', '유': '금', '술': '흙', '해': '물'
        };
        return elementMap[branch] || '';
    }

    updateTraits(traits) {
        // 성향 정보 업데이트
        const tendencyTexts = document.querySelectorAll('.tendency-text');
        if (traits.traits && tendencyTexts.length > 0) {
            traits.traits.slice(0, 6).forEach((trait, index) => {
                if (tendencyTexts[index]) {
                    tendencyTexts[index].textContent = trait;
                }
            });
        }
    }

    updateAnalysisDescriptions(sajuData) {
        const fiveElement = sajuData.five_element;
        const dayStem = sajuData.day_stem;
        const dayBranch = sajuData.day_branch;
        const dayPillar = sajuData.day_pillar;

        // 오행 분석 설명
        const fiveElementDesc = document.getElementById('five-element-desc');
        if (fiveElementDesc) {
            fiveElementDesc.textContent = this.getFiveElementDescription(fiveElement);
        }

        // 천간지지 분석 설명
        const stemBranchDesc = document.getElementById('stem-branch-desc');
        if (stemBranchDesc) {
            stemBranchDesc.textContent = this.getStemBranchDescription(dayStem, dayBranch);
        }

        // 일주 분석 설명
        const dayPillarDesc = document.getElementById('day-pillar-desc');
        if (dayPillarDesc) {
            dayPillarDesc.textContent = this.getDayPillarDescription(dayPillar);
        }
    }

    getFiveElementDescription(fiveElement) {
        const descriptions = {
            '나무': '창의적이고 성장 지향적인 성격으로, 새로운 아이디어를 제시하고 팀을 이끄는 리더십이 뛰어납니다.',
            '불': '열정적이고 추진력이 강한 성격으로, 프로젝트를 성공적으로 완수하는 능력이 뛰어납니다.',
            '흙': '안정적이고 신중한 성격으로, 팀의 조화를 이끌고 체계적인 관리 능력이 뛰어납니다.',
            '금': '논리적이고 분석적인 성격으로, 데이터 기반의 의사결정과 정확한 업무 처리 능력이 뛰어납니다.',
            '물': '유연하고 공감능력이 뛰어난 성격으로, 소통과 협업에 뛰어난 강점을 보입니다.'
        };
        return descriptions[fiveElement] || '분석 중...';
    }

    getStemBranchDescription(dayStem, dayBranch) {
        return `${dayStem}${dayBranch}의 조합으로, 균형 잡힌 사고와 실행력을 겸비한 성격을 나타냅니다.`;
    }

    getDayPillarDescription(dayPillar) {
        return `${dayPillar} 일주는 핵심적인 성격 특성을 나타내며, 직무에서의 강점과 약점을 파악하는 중요한 지표입니다.`;
    }

    updateTip(fiveElement, dayBranch) {
        const tipContent = document.getElementById('tip-content');
        if (tipContent) {
            const elementName = this.fiveElementNames[fiveElement];
            tipContent.textContent = `태어난 시간의 요소(${elementName})가 '실무 성향'을 많이 좌우합니다. ${this.getTipAdvice(fiveElement)}`;
        }
    }

    getTipAdvice(fiveElement) {
        const advices = {
            '나무': '창의성과 리더십이 강하지만, 팀원들의 의견도 충분히 수렴하세요.',
            '불': '추진력이 강하지만, 신중한 검토와 계획도 함께 고려하세요.',
            '흙': '안정성이 강하지만, 변화와 혁신에도 적극적으로 도전하세요.',
            '금': '논리적 사고가 강하지만, 직관과 감정도 함께 고려하세요.',
            '물': '공감과 소통이 강하지만, 데이터와 비즈니스 지표도 함께 고려하세요.'
        };
        return advices[fiveElement] || '균형 잡힌 접근을 유지하세요.';
    }

    showExampleData() {
        // 사진을 참고한 실제 사주 데이터 표시
        const exampleData = {
            five_element: '불',
            day_stem: '정',
            day_branch: '미', 
            day_pillar: '정미',
            traits: {
                traits: ['열정', '추진력', '창의성', '리더십', '활발함', '관리능력']
            },
            four_pillars: {
                hour: {stem: '을', branch: '사', stem_hanja: '乙', branch_hanja: '巳', ten_god: '편인'},
                day: {stem: '정', branch: '미', stem_hanja: '丁', branch_hanja: '未', ten_god: '비견'},
                month: {stem: '정', branch: '묘', stem_hanja: '丁', branch_hanja: '卯', ten_god: '비견'},
                year: {stem: '갑', branch: '술', stem_hanja: '甲', branch_hanja: '戌', ten_god: '정인'}
            }
        };
        
        this.updateAnalysis(exampleData);
    }

    showError(message) {
        // 에러 메시지 표시
        const container = document.getElementById('saju_app_container');
        container.innerHTML = `
            <header class="bg-gradient-to-r from-purple-600 via-pink-500 to-fuchsia-500 text-white p-4">
                <div class="flex items-center gap-2">
                    <i class="fa-solid fa-wand-magic-sparkles text-xl"></i>
                    <h1 class="text-lg font-bold">PM 사주 챗봇</h1>
                </div>
            </header>
            <section class="p-6">
                <div class="text-center text-gray-600">
                    <p>${message}</p>
                    <p class="mt-4"><a href="/chat" class="text-purple-600">채팅 페이지로 돌아가기</a></p>
                </div>
            </section>
        `;
    }
}

// 페이지 로드 시 초기화
document.addEventListener('DOMContentLoaded', function() {
    const sajuAnalysis = new SajuAnalysis();
    sajuAnalysis.loadAnalysisFromURL();
});
