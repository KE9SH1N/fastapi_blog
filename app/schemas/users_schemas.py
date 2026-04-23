from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    hashed_password: str
    user_name: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    user_name: str
    created_at: datetime

    class Config:
        from_attributes = True
    