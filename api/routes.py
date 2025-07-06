from fastapi import APIRouter
from pydantic import BaseModel
from api.engine import run_chain

router = APIRouter()

class ChatRequest(BaseModel):
    user_input: str
    system_prompt: str

@router.post("/")
def chat_endpoint(payload: ChatRequest):
    response = run_chain(payload.user_input, payload.system_prompt)
    return {"response" : response}