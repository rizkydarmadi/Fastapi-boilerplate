from fastapi import APIRouter
from .endpoints import router as role_permission

role_permission_router = APIRouter(prefix="/role_permission")
role_permission_router.include_router(role_permission)
