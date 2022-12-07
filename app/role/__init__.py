from fastapi import APIRouter
from .endpoints import router as role

role_router = APIRouter(prefix="/role")
role_router.include_router(role)
