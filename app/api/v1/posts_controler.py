from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.posts_schemas import PostCreate, PostResponse 
from ...database import get_db
from app.services import posts_services

posts_router = APIRouter(prefix="/posts", tags=["posts"])

@posts_router.post("/new", response_model=PostResponse)
def create(post: PostCreate, db: Session = Depends(get_db)):
    return posts_services.create_post(db, post)
