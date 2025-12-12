import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Mengambil URL database dari environment variable
# Format: postgresql://user:password@host/dbname
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Buat engine koneksi
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Buat session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class untuk semua model database
Base = declarative_base()

# Helper function untuk dependency injection di main.py
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()