# Pydantic schemas for user-related data.

from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    """Schema for user registration."""
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserLogin(BaseModel):
    """Schema for user login."""
    email: EmailStr
    password: str

class UserInDB(BaseModel):
    """Schema for representing a user from the database."""
    id: int
    email: EmailStr
    
    class Config:
        orm_mode = True