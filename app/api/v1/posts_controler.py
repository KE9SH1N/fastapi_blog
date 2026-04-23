from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.schemas.posts_schemas import PostCreate, PostResponse 
from ...database import get_db
from app.services import posts_services
from app.schemas.pagination_schemas import PaginatedResponse

posts_router = APIRouter(prefix="/posts", tags=["posts"])

@posts_router.post("/new", response_model=PostResponse)
def create(post: PostCreate, db: Session = Depends(get_db)):
    return posts_services.create_post(db, post)


@posts_router.get("/get_all_posts", response_model=PaginatedResponse[PostResponse])
def list_posts(
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    return posts_services.get_posts(db, limit, offset)