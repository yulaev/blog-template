from fastapi import FastAPI
from app.routers import router as posts_router

app = FastAPI()

app.include_router(posts_router)