
from fastapi import FastAPI

from app.db import Base, engine

# from .routes import user
from app.api.router import api_router
from app.models import *
from app.core.startup import startup_seed

app = FastAPI()

app.include_router(api_router)


# Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running"}


@app.on_event("startup")
def startup_event():
    startup_seed()