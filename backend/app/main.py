from typing import List
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import dari module lokal
from app.schemas import ReviewInput, ReviewAnalysisResult, ReviewResponse
from app.services.sentiment import analyze_sentiment_hf
from app.services.gemini import extract_key_points_gemini
from app import models
from app.database import engine, get_db

# 1. Buat Tabel Database Otomatis (jika belum ada)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Review Analyzer API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API is running with PostgreSQL integration."}

# --- ENDPOINT: GET Reviews (Dari Database) ---
@app.get("/api/reviews", response_model=List[ReviewResponse])
def get_all_reviews(db: Session = Depends(get_db)):
    """
    Mengambil semua data review yang tersimpan di PostgreSQL.
    """
    # Query ke database (SELECT * FROM reviews)
    reviews = db.query(models.Review).all()
    return reviews

# --- ENDPOINT: POST Review (Simpan ke Database) ---
@app.post("/api/analyze-review", response_model=ReviewAnalysisResult)
async def analyze_review(payload: ReviewInput, db: Session = Depends(get_db)):
    """
    Menerima text review, analisis sentiment & key points, 
    lalu simpan hasilnya ke PostgreSQL.
    """
    review_text = payload.review_text
    
    if not review_text or len(review_text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Review text cannot be empty")

    # 1. Panggil Hugging Face
    sentiment_result = analyze_sentiment_hf(review_text)
    
    # 2. Panggil Gemini
    key_points_result = extract_key_points_gemini(review_text)
    
    # 3. Buat Object Model Database
    new_review = models.Review(
        review_text=review_text,
        sentiment_label=sentiment_result['label'],
        sentiment_score=sentiment_result['score'],
        key_points=key_points_result  # SQLAlchemy & JSON column handle list -> json
    )
    
    # 4. Simpan ke Database
    db.add(new_review)
    db.commit()      # Commit transaksi
    db.refresh(new_review) # Refresh untuk mendapatkan ID yang digenerate DB
    
    # 5. Return hasil (Pydantic akan memparsing object SQLAlchemy ini)
    return new_review