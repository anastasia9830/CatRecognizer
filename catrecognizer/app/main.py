from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_router import router

app = FastAPI(title="CatRecognizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
