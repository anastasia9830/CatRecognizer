from fastapi import APIRouter, File, UploadFile
from app.services.prediction import predict_breed
from app.schemas.prediction_output import PredictionResponse

from PIL import Image
import io

router = APIRouter()

@router.post("/", response_model = PredictionResponse)
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    breed, confidence = predict_breed(image)
    return {"breed": breed, "confidence": confidence}