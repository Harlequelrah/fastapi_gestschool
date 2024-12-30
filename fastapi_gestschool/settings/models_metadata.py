from fastapi_gestschool.teacher import metadata as teacher_metadata
from fastapi_gestschool.profile import metadata as profile_metadata
from sqlalchemy import MetaData

target_metadata = MetaData()

# target_metadata = Base.metadata
target_metadata = teacher_metadata
target_metadata = profile_metadata
# target_metadata = logger_model.Base.metadata
# target_metadata = user_model.Base.metadata
