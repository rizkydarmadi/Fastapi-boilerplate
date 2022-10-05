from fastapi import APIRouter
from .endpoints import router as auth

user = APIRouter(prefix='/auth')
user.include_router(auth)