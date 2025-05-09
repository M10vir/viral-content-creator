from fastapi import APIRouter, HTTPException
from app.services.trending_insight_generator import generate_trending_ai_insight

router = APIRouter()

@router.get("/generate-trending-insight", summary="Generate trending AI insights")
async def get_trending_insight():
    try:
        insight = generate_trending_ai_insight()
        return {"insight": insight}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating insight: {str(e)}") 
