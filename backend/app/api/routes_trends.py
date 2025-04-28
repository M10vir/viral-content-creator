# backend/app/api/routes_trends.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/dummy-trends")
def dummy_trends():
    return {"message": "Trends route working!"}
