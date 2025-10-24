# 만세력 기반 사주 계산기
# 생년월일시를 입력하면 만세력에 기반한 사주 분석을 제공

class SajuCalculator:
    def __init__(self):
        # 천간 10개
        self.heavenly_stems = ['갑', '을', '병', '정', '무', '기', '경', '신', '임', '계']
        # 지지 12개
        self.earthly_branches = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']
        # 오행 매핑 (천간 기준)
        self.five_elements = {
            '갑': '나무', '을': '나무', '병': '불', '정': '불', '무': '흙', '기': '흙',
            '경': '금', '신': '금', '임': '물', '계': '물'
        }
        # 지지 오행 매핑
        self.earthly_five_elements = {
            '자': '물', '축': '흙', '인': '나무', '묘': '나무', '진': '흙', '사': '불',
            '오': '불', '미': '흙', '신': '금', '유': '금', '술': '흙', '해': '물'
        }
        
        # 천간 한자 매핑
        self.heavenly_stems_hanja = {
            '갑': '甲', '을': '乙', '병': '丙', '정': '丁', '무': '戊', 
            '기': '己', '경': '庚', '신': '辛', '임': '壬', '계': '癸'
        }
        
        # 지지 한자 매핑
        self.earthly_branches_hanja = {
            '자': '子', '축': '丑', '인': '寅', '묘': '卯', '진': '辰', '사': '巳',
            '오': '午', '미': '未', '신': '申', '유': '酉', '술': '戌', '해': '亥'
        }
        
        # 십성 계산을 위한 오행 관계
        self.ten_gods = {
            '비견': '같은 오행, 같은 음양',
            '겁재': '같은 오행, 다른 음양', 
            '식신': '생하는 오행, 같은 음양',
            '상관': '생하는 오행, 다른 음양',
            '편재': '극하는 오행, 같은 음양',
            '정재': '극하는 오행, 다른 음양',
            '편관': '극당하는 오행, 같은 음양',
            '정관': '극당하는 오행, 다른 음양',
            '편인': '생당하는 오행, 같은 음양',
            '정인': '생당하는 오행, 다른 음양'
        }
        
        # 십성 계산을 위한 오행 상생/상극 관계
        self.five_element_relations = {
            '나무': {'생': '불', '극': '흙', '생당': '물', '극당': '금'},
            '불': {'생': '흙', '극': '금', '생당': '나무', '극당': '물'},
            '흙': {'생': '금', '극': '물', '생당': '불', '극당': '나무'},
            '금': {'생': '물', '극': '나무', '생당': '흙', '극당': '불'},
            '물': {'생': '나무', '극': '불', '생당': '금', '극당': '흙'}
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
        
        # 만세력 기반 절기 정보 (양력 기준)
        self.seasons = {
            1: {'start': 6, 'name': '소한'},      # 1월 6일경
            2: {'start': 4, 'name': '입춘'},       # 2월 4일경  
            3: {'start': 6, 'name': '경칩'},      # 3월 6일경
            4: {'start': 5, 'name': '청명'},      # 4월 5일경
            5: {'start': 6, 'name': '입하'},      # 5월 6일경
            6: {'start': 6, 'name': '망종'},      # 6월 6일경
            7: {'start': 7, 'name': '소서'},      # 7월 7일경
            8: {'start': 8, 'name': '입추'},     # 8월 8일경
            9: {'start': 8, 'name': '백로'},      # 9월 8일경
            10: {'start': 8, 'name': '한로'},     # 10월 8일경
            11: {'start': 7, 'name': '입동'},     # 11월 7일경
            12: {'start': 7, 'name': '대설'}      # 12월 7일경
        }
    
    def get_lunar_month(self, year, month, day):
        """양력을 음력으로 변환하는 간단한 계산"""
        # 실제로는 복잡한 음력 변환 알고리즘이 필요하지만, 
        # 여기서는 간단한 근사치를 사용
        lunar_month_offset = {
            1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3,
            7: 3, 8: 4, 9: 4, 10: 5, 11: 5, 12: 6
        }
        
        # 간단한 음력 월 계산 (실제로는 더 복잡함)
        lunar_month = month + lunar_month_offset.get(month, 0)
        if lunar_month > 12:
            lunar_month -= 12
            
        return lunar_month
    
    def get_season_info(self, month, day):
        """절기 정보 반환"""
        season_info = self.seasons.get(month, {})
        if day >= season_info.get('start', 1):
            return season_info.get('name', '')
        return ''
    
    def calculate_four_pillars(self, year, month, day, hour, minute=0):
        """만세력 기반 사주 계산 (년주, 월주, 일주, 시주)"""
        try:
            from datetime import datetime
            
            # 년주 계산 (년도 기준)
            year_stem_index = (year - 4) % 10  # 1900년이 경자년 기준
            year_branch_index = (year - 4) % 12
            year_stem = self.heavenly_stems[year_stem_index]
            year_branch = self.earthly_branches[year_branch_index]
            
            # 월주 계산 (음력 월 기준)
            lunar_month = self.get_lunar_month(year, month, day)
            month_stem_index = (year_stem_index * 2 + lunar_month) % 10
            month_branch_index = (lunar_month + 1) % 12
            month_stem = self.heavenly_stems[month_stem_index]
            month_branch = self.earthly_branches[month_branch_index]
            
            # 일주 계산 (만세력 기준)
            # 1900년 1월 1일을 기준으로 한 정확한 일수 계산
            base_date = datetime(1900, 1, 1)
            target_date = datetime(year, month, day)
            days_diff = (target_date - base_date).days
            
            # 일간 계산 (10일 주기)
            day_stem_index = (days_diff + 1) % 10
            day_stem = self.heavenly_stems[day_stem_index]
            
            # 일지 계산 (12일 주기)
            day_branch_index = (days_diff + 1) % 12
            day_branch = self.earthly_branches[day_branch_index]
            
            # 시주 계산 (시간 기준)
            hour_branch_index = ((hour + 1) // 2) % 12  # 2시간 단위
            hour_stem_index = (day_stem_index * 2 + hour_branch_index) % 10
            hour_stem = self.heavenly_stems[hour_stem_index]
            hour_branch = self.earthly_branches[hour_branch_index]
            
            return {
                'year': {'stem': year_stem, 'branch': year_branch, 'pillar': year_stem + year_branch},
                'month': {'stem': month_stem, 'branch': month_branch, 'pillar': month_stem + month_branch},
                'day': {'stem': day_stem, 'branch': day_branch, 'pillar': day_stem + day_branch},
                'hour': {'stem': hour_stem, 'branch': hour_branch, 'pillar': hour_stem + hour_branch}
            }
            
        except Exception as e:
            print(f"사주 계산 오류: {e}")
            return None
    
    def calculate_saju(self, year, month, day, hour, minute=0):
        """만세력 기반 사주 정보를 계산"""
        try:
            # 만세력 기반 사주 계산
            four_pillars = self.calculate_four_pillars(year, month, day, hour, minute)
            
            if not four_pillars:
                return None
            
            # 일주 정보 추출
            day_stem = four_pillars['day']['stem']
            day_branch = four_pillars['day']['branch']
            day_pillar = four_pillars['day']['pillar']
            
            # 오행 계산 (일간 기준)
            five_element = self.five_elements[day_stem]
            
            # 절기 정보
            season = self.get_season_info(month, day)
            
            return {
                'five_element': five_element,
                'day_stem': day_stem,
                'day_branch': day_branch,
                'day_pillar': day_pillar,
                'four_pillars': four_pillars,
                'season': season,
                'lunar_month': self.get_lunar_month(year, month, day)
            }
            
        except Exception as e:
            print(f"사주 계산 오류: {e}")
            return None
    
    def get_five_element(self, year, month, day, hour, minute=0):
        """생년월일시분을 입력받아 해당하는 오행을 반환 (기존 호환성 유지)"""
        result = self.calculate_saju(year, month, day, hour, minute)
        if result:
            return result['five_element']
        return None
    
    def get_five_element_traits(self, five_element):
        """오행에 해당하는 성향과 특징 정보를 반환"""
        if five_element in self.five_element_traits:
            return self.five_element_traits[five_element]
        return None
    
    def calculate_ten_god(self, day_stem, target_stem):
        """일간을 기준으로 타겟 천간의 십성 계산"""
        day_element = self.five_elements[day_stem]
        target_element = self.five_elements[target_stem]
        
        # 음양 판단 (갑, 병, 무, 경, 임은 양, 나머지는 음)
        day_yin_yang = '양' if day_stem in ['갑', '병', '무', '경', '임'] else '음'
        target_yin_yang = '양' if target_stem in ['갑', '병', '무', '경', '임'] else '음'
        
        # 같은 오행인 경우
        if day_element == target_element:
            if day_yin_yang == target_yin_yang:
                return '비견'
            else:
                return '겁재'
        
        # 오행 관계에 따른 십성 계산
        relations = self.five_element_relations[day_element]
        
        if target_element == relations['생']:
            if day_yin_yang == target_yin_yang:
                return '식신'
            else:
                return '상관'
        elif target_element == relations['극']:
            if day_yin_yang == target_yin_yang:
                return '편재'
            else:
                return '정재'
        elif target_element == relations['극당']:
            if day_yin_yang == target_yin_yang:
                return '편관'
            else:
                return '정관'
        elif target_element == relations['생당']:
            if day_yin_yang == target_yin_yang:
                return '편인'
            else:
                return '정인'
        
        return '알수없음'
    
    def calculate_branch_ten_god(self, day_stem, target_branch):
        """일간을 기준으로 타겟 지지의 십성 계산"""
        day_element = self.five_elements[day_stem]
        target_element = self.earthly_five_elements[target_branch]
        
        # 음양 판단 (갑, 병, 무, 경, 임은 양, 나머지는 음)
        day_yin_yang = '양' if day_stem in ['갑', '병', '무', '경', '임'] else '음'
        
        # 지지의 음양 판단 (자, 인, 진, 오, 신, 술은 양, 나머지는 음)
        branch_yin_yang = '양' if target_branch in ['자', '인', '진', '오', '신', '술'] else '음'
        
        # 같은 오행인 경우
        if day_element == target_element:
            if day_yin_yang == branch_yin_yang:
                return '비견'
            else:
                return '겁재'
        
        # 오행 관계에 따른 십성 계산
        relations = self.five_element_relations[day_element]
        
        if target_element == relations['생']:
            if day_yin_yang == branch_yin_yang:
                return '식신'
            else:
                return '상관'
        elif target_element == relations['극']:
            if day_yin_yang == branch_yin_yang:
                return '편재'
            else:
                return '정재'
        elif target_element == relations['극당']:
            if day_yin_yang == branch_yin_yang:
                return '편관'
            else:
                return '정관'
        elif target_element == relations['생당']:
            if day_yin_yang == branch_yin_yang:
                return '편인'
            else:
                return '정인'
        
        return '알수없음'
    

# 사용 예시
if __name__ == "__main__":
    calculator = SajuCalculator()
    
    # 만세력 기반 사주 분석
    saju_result = calculator.calculate_saju(1997, 5, 7, 21, 30)  # 1997년 5월 7일 오후 9시 30분
    if saju_result:
        print("=== 만세력 기반 사주 분석 ===")
        print(f"오행: {saju_result['five_element']}")
        print(f"일간(천간): {saju_result['day_stem']}")
        print(f"일지(지지): {saju_result['day_branch']}")
        print(f"일주: {saju_result['day_pillar']}")
        print(f"절기: {saju_result['season']}")
        print(f"음력월: {saju_result['lunar_month']}월")
        
        # 사주 기둥 정보
        four_pillars = saju_result['four_pillars']
        print(f"\n=== 사주 기둥 (만세력) ===")
        print(f"년주: {four_pillars['year']['pillar']} ({four_pillars['year']['stem']} + {four_pillars['year']['branch']})")
        print(f"월주: {four_pillars['month']['pillar']} ({four_pillars['month']['stem']} + {four_pillars['month']['branch']})")
        print(f"일주: {four_pillars['day']['pillar']} ({four_pillars['day']['stem']} + {four_pillars['day']['branch']})")
        print(f"시주: {four_pillars['hour']['pillar']} ({four_pillars['hour']['stem']} + {four_pillars['hour']['branch']})")
        
        # 오행 상세 정보
        traits = calculator.get_five_element_traits(saju_result['five_element'])
        if traits:
            print(f"\n=== {traits['name']} {traits['emoji']} 성격 특징 ===")
            print(f"특징: {', '.join(traits['traits'])}")
            print(f"설명: {traits['description']}")
            print(f"강점: {traits['strengths']}")
            print(f"약점: {traits['weaknesses']}")
    
    # 기존 호환성 테스트
    print("\n=== 기존 방식 테스트 ===")
    old_result = calculator.get_five_element(1997, 5, 7, 21, 30)
    print(f"오행만: {old_result}")