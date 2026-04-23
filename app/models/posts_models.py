from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from ..database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)


