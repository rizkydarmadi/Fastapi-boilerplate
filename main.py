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

app.include_router(user)
@app.get("/")
async def hello():
    return {'Hello': "You Make Me Happy"}