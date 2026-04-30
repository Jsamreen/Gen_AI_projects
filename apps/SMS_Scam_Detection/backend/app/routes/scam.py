from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import analyze_sms_with_ai

router = APIRouter(prefix="/scam", tags=["Scam Detection"])


class SMSRequest(BaseModel):
    message: str
    sender_known: str


@router.post("/analyze")
def analyze_sms(data: SMSRequest):
    result = analyze_sms_with_ai(data.message, data.sender_known)
    return result