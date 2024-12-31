from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form

from .enum import GenderEnum
class ProfileBase(BaseModel):
    age:int=Field(example=20)
    gender:GenderEnum=Field(example=GenderEnum.Female, default=GenderEnum.NOT_SPECIFIED)
    birth_date: datetime = Field(example=datetime.datetime(2000, 1, 1, 10, 30))

class ProfileCreate(ProfileBase):
    teacher_id:int=Field(example=1)
class ProfilUpdate(BaseModel):
    teacher_id: Optional[int] = Field(example=1)
    gender:Optional[GenderEnum] = Field(example=GenderEnum.Male)
    birth_date: Optional[datetime] = Field(example=datetime.datetime(2000, 1, 1, 10, 30))
    age:Optional[int]=Field(example=30)

class ProfilePydanticModel(BaseModel):
    id:int
    age:int
    gender:GenderEnum
    birth_date:datetime
    teacher_id:int
    class setting :
        from_orm=True
