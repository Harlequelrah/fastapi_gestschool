
from fastapi_gestschool.profile.model import Profile
from fastapi_gestschool.profile.schema import ProfileCreateModel,ProfileUpdateModel
from harlequelrah_fastapi.crud.crud_forgery import CrudForgery
from fastapi_gestschool.settings.database import authentication

profile_crud = CrudForgery(
    entity_name="profile",
    authentication=authentication,
    SQLAlchemyModel=Profile,
    CreatePydanticModel=ProfileCreateModel,
    UpdatePydanticModel=ProfileUpdateModel,
)
