
from fastapi import FastAPI

from app.db import Base, engine

# from .routes import user
from app.api.router import api_router
from app.models import *

app = FastAPI()

app.include_router(api_router)


# Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running"}