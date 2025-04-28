# backend/app/api/routes_content.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/dummy-content")
def dummy_content():
    return {"message": "Content route working!"}
