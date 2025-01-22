from sqlalchemy import (
    Column,
    Enum,
    Integer,
    DateTime,
    ForeignKey,
    Enum
)
from fastapi_gestschool.settings.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .enum import GenderEnum


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    age=Column(Integer,index=True,nullable=False)
    gender=Column(Enum(GenderEnum),index=True,nullable=False,default=GenderEnum.NOT_SPECIFIED)
    birth_date=Column(DateTime)
    teacher_id=Column(Integer,ForeignKey('teachers.id'))
    teacher=relationship("Teacher",back_populates="profile")


metadata= Base.metadata

