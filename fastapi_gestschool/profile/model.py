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
from fastapi_gestschool.teacher.model import Teacher
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    age=Column(Integer,index=True,nullable=False)
    gender=Column(String,index=True,nullable=False)
    birth_date=Column(DateTime)
    teacher_id=Column(Integer,ForeignKey('users.id'))
    teacher=relationship("Teacher",back_populates="profile")




