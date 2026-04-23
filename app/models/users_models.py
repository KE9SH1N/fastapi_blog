from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    user_name = Column(String, index=True)
    created_at = Column(DateTime, server_default="CURRENT_TIMESTAMP")


