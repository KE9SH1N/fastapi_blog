from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
    