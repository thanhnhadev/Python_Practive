from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv() 

router = APIRouter()

# Lấy API key từ biến môi trường
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("⚠️ Chưa có OPENAI_API_KEY trong môi trường!")

client = OpenAI(api_key=OPENAI_API_KEY)

class ChatRequest(BaseModel):
    message: str

@router.post("/chatting")
async def chat_with_ai(request: ChatRequest):
    """
    Gửi tin nhắn đến OpenAI và nhận phản hồi.
    """
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # hoặc model bạn có quyền truy cập
            messages=[
                {"role": "system", "content": "Bạn là một trợ lý tài chính thân thiện."},
                {"role": "user", "content": request.message},
            ],
        )
        reply = completion.choices[0].message.content
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
