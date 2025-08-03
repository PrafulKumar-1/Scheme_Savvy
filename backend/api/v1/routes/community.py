# FILE: backend/api/v1/routes/community.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/questions")
def get_questions():
    # Placeholder for community Q&A feature
    return {"message": "Community Q&A feature coming soon!"}

@router.post("/questions")
def ask_question():
    return {"message": "Community Q&A feature coming soon!"}