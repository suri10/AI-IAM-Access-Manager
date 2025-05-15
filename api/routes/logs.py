from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from engine.analyzer import analyze_log

router = APIRouter(prefix="/logs", tags=["logs"])

class LogRequest(BaseModel):
    log: str

@router.post("/analyze")
async def analyze(log_request: LogRequest):
    """
    Analyze the provided log and return threat score + action.
    Slack alerts are triggered inside the analyzer if needed.
    """
    result = analyze_log(log_request.log)
    if result is None:
        raise HTTPException(status_code=400, detail="Invalid log")
    return result
