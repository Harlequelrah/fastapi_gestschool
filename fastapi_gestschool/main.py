from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from fastapi_gestschool.settings.database import engine, authentication, sessionLocal
from fastapi_gestschool.settings.models_metadata import target_metadata
from harlequelrah_fastapi.middleware.error_middleware import ErrorHandlingMiddleware
# from myproject.todolistapp.route import app_todolist

app = FastAPI()

target_metadata.create_all(bind=engine)
@app.get("/")
async def hello():
    return {"message": "Hello, World!"}

# app.include_router(app_todolist)
app.add_middleware(
    ErrorHandlingMiddleware,
)

