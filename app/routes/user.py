from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import Base, SessionLocal, engine, get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/new", response_model=schemas.UserResponse)
def create(user:schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/get_all_users", response_model=list[schemas.UserResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/search_user", response_model=list[schemas.UserResponse])
def read_all_byName(name:str, db: Session = Depends(get_db)):
    return crud.get_users_by_name(db, name)

@router.get("/{user_id}", response_model=schemas.UserResponse)
def read_one(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"} 
