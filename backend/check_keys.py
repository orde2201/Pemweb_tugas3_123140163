import os
import google.generativeai as genai
import requests
from dotenv import load_dotenv

# 1. Coba load .env
load_dotenv()

print("--- DIAGNOSA KONEKSI AI ---")

# 2. Cek Token Hugging Face
hf_token = os.getenv("HF_API_TOKEN")
if not hf_token:
    print("❌ HF_API_TOKEN: TIDAK DITEMUKAN di .env")
else:
    print(f"✅ HF_API_TOKEN: Terdeteksi ({hf_token[:5]}...)")
    # Test Request ke Hugging Face
    try:
        headers = {"Authorization": f"Bearer {hf_token}"}
        response = requests.get("https://huggingface.co/api/whoami-v2", headers=headers)
        if response.status_code == 200:
            print("   -> Koneksi Hugging Face: SUKSES (Valid)")
        else:
            print(f"   -> Koneksi Hugging Face: GAGAL (Status: {response.status_code})")
            print("   -> Pastikan token Anda bertipe 'Read' dan tidak kadaluarsa.")
    except Exception as e:
        print(f"   -> Koneksi Hugging Face: ERROR ({e})")

# 3. Cek Token Gemini
gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    print("❌ GEMINI_API_KEY: TIDAK DITEMUKAN di .env")
else:
    print(f"✅ GEMINI_API_KEY: Terdeteksi ({gemini_key[:5]}...)")
    # Test Request ke Gemini
    try:
        genai.configure(api_key=gemini_key)
        # Gunakan model 'gemini-1.5-flash' yang lebih stabil untuk tier gratis
        model = genai.GenerativeModel('gemini-1.5-flash') 
        response = model.generate_content("Tes koneksi.")
        print("   -> Koneksi Gemini: SUKSES")
    except Exception as e:
        print(f"   -> Koneksi Gemini: GAGAL")
        print(f"   -> Pesan Error: {e}")

print("---------------------------")