from fastapi import APIRouter, HTTPException
from app.services.auto_prompt_generator import generate_trending_prompt

router = APIRouter()

@router.get("/generate-auto-prompt", summary="Generate AI-related auto prompt")
def get_auto_prompt():
    try:
        prompt = generate_trending_prompt()
        print("Generated Prompt:", prompt)  # Add this for CLI visibility
        return {"auto_prompt": prompt or "No prompt generated"}
    except Exception as e:
        print("Error:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

