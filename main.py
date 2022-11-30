from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.user import user

app = FastAPI(title='Title FastAPI')

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=CORS_ALLOWED_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
async def hello():
    return {'Hello': "You Make Me Happy"}

app.include_router(user)

from app.role import role_router
app.include_router(role_router)

from app.permission import permission_router
app.include_router(permission_router)

from app.role_permission import role_permission_router
app.include_router(role_permission_router)