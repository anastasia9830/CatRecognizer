from fastapi import APIRouter
from app.api.endpoints import predict

router = APIRouter()

router.include_router(predict.router, prefix = "/predict", tags = ["Prediction"])