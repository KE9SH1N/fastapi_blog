from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from app.db.dependencies import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/new", response_model=schemas.UserResponse)
def create(user:schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


