from fastapi_gestschool.teacher.crud import teacher_crud
from fastapi_gestschool.teacher.schema import TeacherPydanticModel
from elrahapi.router.router_provider import CustomRouterProvider

router_provider= CustomRouterProvider(
    prefix="/teachers",
    tags=["teachers"],
    PydanticModel=TeacherPydanticModel,
    crud=teacher_crud
)
app_teacher = router_provider.get_public_router()

