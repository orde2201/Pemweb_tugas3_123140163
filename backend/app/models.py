from sqlalchemy import Column, Integer, String, Float, Text, JSON
from .database import Base

class Review(Base):
    __tablename__ = "reviews"

    # Kita gunakan Integer auto-increment untuk ID agar lebih efisien di DB
    # Pydantic schema (id: str) akan otomatis mengkonversi int ini menjadi string saat response.
    id = Column(Integer, primary_key=True, index=True)
    
    review_text = Column(Text, nullable=False)
    sentiment_label = Column(String, nullable=False) # POSITIVE, NEGATIVE, NEUTRAL
    sentiment_score = Column(Float, nullable=False)
    
    # Menyimpan list key_points sebagai JSON Array
    key_points = Column(JSON, nullable=True)