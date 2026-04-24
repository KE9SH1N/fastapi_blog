from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db import Base

class Permissions(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)

    # roles = relationship(
    #     "Roles",
    #     secondary="role_permissions",
    #     back_populates="permissions"
    # )