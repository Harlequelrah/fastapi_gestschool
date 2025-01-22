
from fastapi_gestschool.teacher.model import Teacher
from fastapi_gestschool.teacher.schema import TeacherCreateModel,TeacherUpdateModel
from harlequelrah_fastapi.crud.crud_forgery import CrudForgery
from fastapi_gestschool.settings.database import authentication
from fastapi_gestschool.profile import Profile
teacher_crud = CrudForgery(
    entity_name="teacher",
    authentication=authentication,
    SQLAlchemyModel=Teacher,
    CreatePydanticModel=TeacherCreateModel,
    UpdatePydanticModel=TeacherUpdateModel,
    Linked_Classes=[
        {'profile':Profile}
    ]
)
