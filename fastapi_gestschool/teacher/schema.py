from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi_gestschool.profile.schema import ProfileMetaModel,ProfileCreateModel,ProfileBase


class TeacherBaseModel(BaseModel):
    email:str=Field(example="user@example.com")
    firstname:str=Field(example="John")
    lastname:str=Field(example="DOE")

class TeacherCreateModel(TeacherBaseModel):
    profile : ProfileBase

class TeacherUpdateModel(BaseModel):
    email:Optional[str]=Field(example="user@example.com",default=None)
    firstname:Optional[str]=Field(example="John",default=None)
    lastname:Optional[str]=Field(example="DOE",default=None)

class TeacherPydanticModel(TeacherCreateModel):
    id : int
    profile : Optional[ProfileMetaModel]

class TeacherMetaModel(BaseModel):
    email:str
    firstname:str
    lastname:str
