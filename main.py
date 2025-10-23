from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI

# 환경변수 로드
load_dotenv()

app = FastAPI()

# 정적 파일 서빙 설정
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 요청 모델 정의
class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/chat/gpt-3.5-turbo")
async def chat_gpt35_turbo(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": request.message}
            ],
            max_tokens=1000
        )
        return {
            "model": "gpt-3.5-turbo",
            "response": response.choices[0].message.content,
            "status": "success"
        }
    except Exception as e:
        return {
            "model": "gpt-3.5-turbo",
            "error": str(e),
            "status": "error"
        }

@app.post("/chat/gpt-4o")
async def chat_gpt4o(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": request.message}
            ],
            max_tokens=1000
        )
        return {
            "model": "gpt-4o",
            "response": response.choices[0].message.content,
            "status": "success"
        }
    except Exception as e:
        return {
            "model": "gpt-4o",
            "error": str(e),
            "status": "error"
        }

@app.post("/chat/gpt-4o-mini")
async def chat_gpt4o_mini(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": request.message}
            ],
            max_tokens=1000
        )
        return {
            "model": "gpt-4o-mini",
            "response": response.choices[0].message.content,
            "status": "success"
        }
    except Exception as e:
        return {
            "model": "gpt-4o-mini",
            "error": str(e),
            "status": "error"
        }

@app.post("/chat/gpt-4-turbo")
async def chat_gpt4_turbo(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "user", "content": request.message}
            ],
            max_tokens=1000
        )
        return {
            "model": "gpt-4-turbo",
            "response": response.choices[0].message.content,
            "status": "success"
        }
    except Exception as e:
        return {
            "model": "gpt-4-turbo",
            "error": str(e),
            "status": "error"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
