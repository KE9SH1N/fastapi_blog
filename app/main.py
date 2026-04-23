
from fastapi import FastAPI

from .database import Base, engine
from .routes import user

app = FastAPI()

app.include_router(user.router)


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running"}