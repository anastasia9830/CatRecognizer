from pydantic import BaseModel

class PredictionResponse(BaseModel):
    breed: str
    confidence: float