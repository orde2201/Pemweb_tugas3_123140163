from pydantic import BaseModel
from typing import List

class ReviewInput(BaseModel):
    review_text: str

class ReviewAnalysisResult(BaseModel):
    sentiment_label: str  # POSITIVE, NEGATIVE, NEUTRAL
    sentiment_score: float
    key_points: List[str]
    
    class Config:
        from_attributes = True

# Schema baru untuk respon GET (Data lengkap dengan ID dan Text asli)
class ReviewResponse(ReviewAnalysisResult):
    id: str
    review_text: str