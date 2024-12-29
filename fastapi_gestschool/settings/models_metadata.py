# from fastapi_gestschool.teacher.model import Base as teacher_base
# from fastapi_gestschool.profile.model import  Base as profile_base
from .database import Base
from sqlalchemy import MetaData
# from userapp import user_model
# from harlequelrah_fastapi.middleware.logapp import log_model


target_metadata = MetaData()
target_metadata = Base.metadata
# target_metadata = profile_base.Base.metadata
# target_metadata = logger_model.Base.metadata
# target_metadata = user_model.Base.metadata
