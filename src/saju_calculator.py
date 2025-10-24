# 단순한 오행 계산기
# 생년월일시를 입력하면 해당하는 오행(물, 금, 불, 흙, 나무) 중 하나를 반환

class SajuCalculator:
    def __init__(self):
        # 천간 10개
        self.heavenly_stems = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
        # 오행 매핑 (천간 기준)
        self.five_elements = {
            '갑': '나무', '을': '나무', '병': '불', '정': '불', '무': '흙', '기': '흙',
            '경': '금', '신': '금', '임': '물', '계': '물'
        }
        
        # 오행별 성향과 특징
        self.five_element_traits = {
            '나무': {
                'name': '목(木)',
                'emoji': '🌳',
                'traits': ['성장', '창의성', '리더십', '도전정신', '활발함'],
                'description': '성장과 발전을 추구하는 활발한 성격으로, 새로운 도전을 즐기고 창의적인 사고를 합니다. 리더십이 강하고 팀을 이끌어가는 능력이 뛰어납니다.',
                'strengths': '창의적 사고, 리더십, 도전정신, 성장 지향적',
                'weaknesses': '성급함, 완벽주의 경향, 타인의 의견을 무시할 수 있음'
            },
            '불': {
                'name': '화(火)',
                'emoji': '🔥',
                'traits': ['열정', '추진력', '활동성', '표현력', '에너지'],
                'description': '강한 열정과 추진력을 가진 활발한 성격으로, 목표를 향해 끊임없이 전진합니다. 표현력이 뛰어나고 주변 사람들에게 에너지를 전달합니다.',
                'strengths': '강한 추진력, 열정, 빠른 실행력, 에너지 전달',
                'weaknesses': '성급함, 인내심 부족, 감정적 기복이 클 수 있음'
            },
            '흙': {
                'name': '토(土)',
                'emoji': '🪨',
                'traits': ['안정성', '신중함', '책임감', '관리능력', '균형감각'],
                'description': '안정적이고 신중한 성격으로, 책임감이 강하고 체계적인 관리 능력이 뛰어납니다. 균형감각이 좋아 팀의 조화를 이끌어냅니다.',
                'strengths': '안정성, 신중함, 책임감, 체계적 관리, 균형감각',
                'weaknesses': '보수적 성향, 변화에 둔감, 결정이 느릴 수 있음'
            },
            '금': {
                'name': '금(金)',
                'emoji': '⚙️',
                'traits': ['논리성', '분석력', '정확성', '체계성', '객관성'],
                'description': '논리적이고 분석적인 사고를 하는 성격으로, 객관적 데이터를 바탕으로 정확한 판단을 내립니다. 체계적이고 정확한 작업을 선호합니다.',
                'strengths': '논리적 사고, 분석력, 정확성, 체계성, 객관성',
                'weaknesses': '감정 표현 부족, 유연성 부족, 완벽주의 경향'
            },
            '물': {
                'name': '수(水)',
                'emoji': '💧',
                'traits': ['유연성', '공감능력', '소통능력', '적응력', '직관력'],
                'description': '유연하고 공감능력이 뛰어난 성격으로, 타인의 감정을 잘 이해하고 소통 능력이 뛰어납니다. 변화에 잘 적응하고 직관력이 강합니다.',
                'strengths': '공감능력, 소통능력, 유연성, 적응력, 직관력',
                'weaknesses': '결정력 부족, 우유부단함, 타인의 의견에 쉽게 휩쓸림'
            }
        }
        
    
    def get_five_element(self, year, month, day, hour, minute=0):
        """생년월일시분을 입력받아 해당하는 오행을 반환"""
        try:
            # 일간(일주의 천간) 계산
            # 간단한 공식: (년도 + 월 + 일 + 시 + 분) % 10
            stem_index = (year + month + day + hour + minute) % 10
            day_stem = self.heavenly_stems[stem_index]
            
            # 해당 천간의 오행 반환
            return self.five_elements[day_stem]
            
        except Exception as e:
            print(f"오행 계산 오류: {e}")
            return None
    
    def get_five_element_traits(self, five_element):
        """오행에 해당하는 성향과 특징 정보를 반환"""
        if five_element in self.five_element_traits:
            return self.five_element_traits[five_element]
        return None
    

# 사용 예시
if __name__ == "__main__":
    calculator = SajuCalculator()
    result = calculator.get_five_element(1997, 5, 7, 21, 30)  # 1997년 5월 7일 오후 9시 30분
    print(f"오행: {result}")