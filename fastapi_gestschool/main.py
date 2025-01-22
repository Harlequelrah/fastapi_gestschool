from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from fastapi_gestschool.settings.database import engine
from fastapi_gestschool.settings.models_metadata import target_metadata
from harlequelrah_fastapi.middleware.error_middleware import ErrorHandlingMiddleware
from fastapi_gestschool.teacher.route import app_teacher
from fastapi_gestschool.profile.route import app_profile

app = FastAPI()
app.include_router(app_profile)
app.include_router(app_teacher)
target_metadata.create_all(bind=engine)
@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

# app.include_router(app_todolist)
app.add_middleware(
    ErrorHandlingMiddleware,
)

