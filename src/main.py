from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from saju_calculator import SajuCalculator

app = FastAPI()

# 정적 파일 서빙 설정
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 오행 계산기 초기화
saju_calculator = SajuCalculator()

# 요청 모델 정의
class SajuRequest(BaseModel):
    birth_date: str  # YYYY-MM-DD 형식
    birth_time: str  # HH:MM 형식
    gender: str      # 남/여
    birth_place: str # 출생지역

@app.get("/")
async def read_root():
    return {"message": "오행 계산기 API"}

@app.get("/chat")
async def chat_page():
    """채팅 페이지 반환"""
    return FileResponse("app/static/chat.html")

@app.post("/saju/analyze")
async def analyze_saju(request: SajuRequest):
    """오행 분석 API - 생년월일시를 받아서 해당하는 오행을 반환"""
    try:
        # 날짜와 시간 파싱
        from datetime import datetime
        
        # 생년월일 파싱
        birth_date_obj = datetime.strptime(request.birth_date, "%Y-%m-%d")
        year = birth_date_obj.year
        month = birth_date_obj.month
        day = birth_date_obj.day
        
        # 출생시간 파싱
        birth_time_obj = datetime.strptime(request.birth_time, "%H:%M")
        hour = birth_time_obj.hour
        minute = birth_time_obj.minute
        
        # 오행 계산
        five_element = saju_calculator.get_five_element(
            year, month, day, hour, minute
        )
        
        if not five_element:
            return {
                "status": "error",
                "error": "오행 계산에 실패했습니다."
            }
        
        # 오행 성향 정보 가져오기
        traits_info = saju_calculator.get_five_element_traits(five_element)
        
        if traits_info:
            message = f"{traits_info['emoji']} 당신의 오행은 '{traits_info['name']}'입니다.\n\n"
            message += f"📋 주요 성향: {', '.join(traits_info['traits'])}\n\n"
            message += f"💪 강점: {traits_info['strengths']}\n\n"
            message += f"⚠️ 주의점: {traits_info['weaknesses']}\n\n"
            message += f"📝 상세 설명: {traits_info['description']}"
        else:
            message = f"당신의 오행은 '{five_element}'입니다."
        
        return {
            "status": "success",
            "birth_date": f"{year}년 {month}월 {day}일 {hour}시 {minute}분",
            "gender": request.gender,
            "birth_place": request.birth_place,
            "five_element": five_element,
            "message": message,
            "traits": traits_info
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)