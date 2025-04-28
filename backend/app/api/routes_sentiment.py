# backend/app/api/routes_sentiment.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/dummy-sentiment")
def dummy_sentiment():
    return {"message": "Sentiment route working!"}
