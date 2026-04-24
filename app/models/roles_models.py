from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from sqlalchemy.orm import relationship

from app.db import Base


class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    
    # user = relationship("User", back_populates="roles")
    # permission = relationship("Permissions", secondary="role_permission", back_populates="roles")


