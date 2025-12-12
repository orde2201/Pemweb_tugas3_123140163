# Product Review Analyzer 🚀

Aplikasi web berbasis AI untuk menganalisis sentimen dan mengekstrak poin penting dari ulasan produk secara otomatis. 

## 📋 Fitur Utama

1. **Analisis Sentimen**  
   Mengklasifikasikan ulasan menjadi **POSITIF**, **NEGATIF**, atau **NETRAL** menggunakan model AI dari **Hugging Face**.

2. **Ekstraksi Poin Penting**  
   Merangkum poin-poin kunci dari ulasan dengan memanfaatkan **Google Gemini AI**.

3. **Penyimpanan Database**  
   Menyimpan hasil analisis secara otomatis ke dalam database **PostgreSQL**.

4. **Antarmuka Responsif**  
   Dibangun dengan **React JS** untuk pengalaman pengguna yang modern dan mudah digunakan.

5. **Sistem Fallback Otomatis**  
   Tetap berfungsi bahkan jika salah satu layanan AI mengalami gangguan, berkat mekanisme fail-safe yang terintegrasi.

## 🛠️ Teknologi yang Digunakan

- **Frontend**: React.js, CSS Modules
- **Backend**: Python FastAPI, Uvicorn
- **Database**: PostgreSQL, SQLAlchemy
- **Layanan AI**: Hugging Face Inference API, Google Generative AI (Gemini)

---

## ⚙️ Persyaratan Sistem

Pastikan perangkat Anda telah terinstal:

- Node.js & npm
- Python 3.9 atau lebih tinggi
- PostgreSQL Server

---

## 🚀 Panduan Instalasi dan Menjalankan

### 1. Persiapan Backend

Masuk ke direktori backend dan instal dependensi yang diperlukan:

```bash
cd backend
pip install -r requirements.txt
```

**Konfigurasi Environment**  
Edit file .env sesuai dengan API kalian 

```env
DATABASE_URL=postgresql://postgres:password_anda@localhost:5432/review_db
HF_API_TOKEN=token_huggingface_anda
GEMINI_API_KEY=api_key_gemini_anda
```

**Menjalankan Server Backend**:

```bash
uvicorn app.main:app --reload
```

Server backend akan berjalan di `http://localhost:8000`.

### 2. Persiapan Frontend

Buka terminal baru, masuk ke folder frontend, dan instal dependensi:

```bash
cd frontend
npm install
```

**Menjalankan Frontend**:

```bash
npm start
```

Aplikasi frontend akan terbuka di `http://localhost:3000`.


**Catatan**: Pastikan untuk mengganti nilai token dan kredensial database di backend/.env dengan milik Anda sendiri. Jangan pernah membagikan informasi rahasia seperti token API atau kata sandi database kepada publik.
