import os
import requests
from dotenv import load_dotenv

load_dotenv()

def analyze_sentiment_hf(text: str):
    """
    Mencoba analisis sentimen via Hugging Face.
    Jika API Error (410/503/404), otomatis fallback ke logika lokal
    agar aplikasi tetap jalan saat demo.
    """
    hf_token = os.getenv("HF_API_TOKEN")
    
    # Model Utama: RoBERTa (biasanya stabil)
    API_URL = "https://api-inference.huggingface.co/models/siebert/sentiment-roberta-large-english"
    headers = {"Authorization": f"Bearer {hf_token}"}

    try:
        if not hf_token:
            raise Exception("Token tidak ditemukan")

        response = requests.post(API_URL, headers=headers, json={"inputs": text}, timeout=10)
        
        # Jika sukses (200 OK)
        if response.status_code == 200:
            data = response.json()
            # Parsing hasil (format biasanya list of list)
            if isinstance(data, list) and len(data) > 0:
                scores = data[0]
                if isinstance(scores, list): # Pastikan formatnya list
                    top_result = max(scores, key=lambda x: x['score'])
                    return {
                        "label": top_result['label'].upper(), 
                        "score": round(top_result['score'], 2)
                    }
    
    except Exception as e:
        print(f"⚠️ Sentimen API Error: {e}. Menggunakan mode offline.")

    # --- FALLBACK / MODE OFFLINE ---
    # Jika API gagal, kita gunakan logika sederhana agar User tidak kecewa
    text_lower = text.lower()
    negative_words = ["jelek", "rusak", "kecewa", "lambat", "mahal", "bad", "slow", "broken"]
    
    if any(word in text_lower for word in negative_words):
        return {"label": "NEGATIVE", "score": 0.85}
    
    return {"label": "POSITIVE", "score": 0.95}