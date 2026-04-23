from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.users_schemas import UserCreate, UserResponse 
from ...database import get_db
from app.services import users_services

users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.post("/new", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return users_services.create_user(db, user)


@users_router.get("/get_all_users", response_model=list[UserResponse])
def read_all(db: Session = Depends(get_db)):
    return users_services.get_users(db)

@users_router.get("/search_user", response_model=list[UserResponse])
def read_all_byName(name:str, db: Session = Depends(get_db)):
    return users_services.get_users_by_name(db, name)

@users_router.get("/{user_id}", response_model=UserResponse)
def read_one(user_id: int, db: Session = Depends(get_db)):
    user = users_services.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@users_router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    user = users_services.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"} 