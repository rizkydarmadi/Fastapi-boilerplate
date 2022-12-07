from fastapi import APIRouter
from .endpoints import router as permission

permission_router = APIRouter(prefix="/permission")
permission_router.include_router(permission)
