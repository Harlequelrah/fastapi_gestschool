from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Table,
)
from fastapi_gestschool.settings.database import Base
from fastapi_gestschool.profile.model import Profile
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    email=Column(String(30),unique=True,index=True)
    firstname=Column(String(50),nullable=False)
    lastname=Column(String(30),nullable=False)
    profil= relationship("Profile",back_populates="teacher",uselist=False)
