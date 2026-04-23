# app/api/v1/router.py

from fastapi import APIRouter

from app.api.v1.posts_controler import posts_router
from app.api.v1.users_controler import users_router

api_router = APIRouter()

api_router.include_router(posts_router, prefix="/api/v1")
api_router.include_router(users_router, prefix="/api/v1")