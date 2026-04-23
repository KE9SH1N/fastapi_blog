from pydantic import BaseModel, Field, field_serializer
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
        
    @field_serializer("created_at")
    def format_created_at(self, value: datetime):
        return value.strftime("%Y-%m-%d, %I:%M %p")
    