# FILE: backend/api/v1/schemas/scheme_schemas.py
from pydantic import BaseModel
from typing import List, Optional

class UserProfile(BaseModel):
    age: int
    state: str
    occupation: str
    income: float  # Annual income in Lakhs
    gender: str

class Scheme(BaseModel):
    scheme_id: str
    scheme_name: str
    ministry: str
    description: str
    benefits: str
    category: str
    official_link: str
    required_documents: List[str]