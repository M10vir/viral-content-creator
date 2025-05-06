from fastapi import APIRouter, HTTPException
from app.services.prompt_generator import generate_ai_news_prompt
from app.services.auto_prompt_generator import generate_trending_prompt

router = APIRouter()

@router.get("/auto-prompt", summary="Generate AI-related auto prompt")
async def auto_prompt():
    try:
        prompt = generate_ai_news_prompt()
        return {"prompt": prompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/generate-auto-prompt", summary="Generate trending AI prompt")
async def get_auto_prompt():
    try:
        prompt = generate_trending_prompt()
        return {"auto_prompt": prompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
