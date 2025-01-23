from fastapi_gestschool.profile.crud import profile_crud
from fastapi_gestschool.profile.schema import ProfilePydanticModel
from elrahapi.router.router_provider import CustomRouterProvider

router_provider= CustomRouterProvider(
    prefix="/profiles",
    tags=["profiles"],
    PydanticModel=ProfilePydanticModel,
    crud=profile_crud
)
app_profile = router_provider.get_public_router()

