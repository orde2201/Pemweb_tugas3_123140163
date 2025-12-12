import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def extract_key_points_gemini(text: str) -> list:
    if not GEMINI_API_KEY:
        return ["API Key Gemini tidak ditemukan."]

    # Daftar model yang akan dicoba satu per satu
    models_to_try = ['gemini-1.5-flash', 'gemini-pro']

    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            prompt = f"Extract 3 short bullet points from: '{text}'. Return ONLY text lines."
            
            response = model.generate_content(prompt)
            
            if response.text:
                # Bersihkan hasil
                points = [
                    line.strip().lstrip('*-• ').strip() 
                    for line in response.text.split('\n') 
                    if line.strip()
                ]
                return points[:5]
                
        except Exception as e:
            print(f"⚠️ Gagal pakai model {model_name}: {e}")
            continue # Coba model berikutnya di list

    # Jika semua model gagal (Fallback terakhir)
    return [
        "Analisis poin otomatis sedang gangguan.",
        "Cek koneksi internet backend.",
        "Review mencakup: " + text[:50] + "..."
    ]