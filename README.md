# 📑 AI Job Recommender System  
### Intelligent Resume Analysis + Job Matching from LinkedIn & Naukri

## 🚀 Overview

The **AI Job Recommender** is a Streamlit-based application that:

- Extracts text from uploaded **PDF CV/Resume**
- Uses **Llama 3.2 via Ollama** to summarize the resume
- Identifies **skill gaps** and **future career roadmap**
- Generates **job search keywords**
- Fetches **real job listings** from LinkedIn & Naukri using **Apify Actors**
- Presents personalized job recommendations to the user

This tool helps job seekers instantly get insights + opportunities tailored to their resume.

---

## ✨ Features

✔ PDF Resume text extraction  
✔ AI-powered resume summary (LLM)  
✔ Missing skill detection  
✔ Future career roadmap generation  
✔ Job keyword extraction  
✔ LinkedIn job scraping via Apify  
✔ Naukri job scraping via Apify  
✔ Clean, interactive UI built using Streamlit  

---

## 🏗️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| LLM | Ollama (Llama3.2) |
| PDF Parsing | PyMuPDF (fitz) |
| Job Data | Apify Actors (LinkedIn, Naukri) |
| Environment | Python 3.12+ • uv |
| Utilities | dotenv |

---

## 📁 Project Structure
job-recommender/
├── app.py
├── pyproject.toml
├── uv.lock
├── .gitignore
├── README.md
├── .python-version
├── src/
│   ├── __init__.py
│   ├── helper.py        # PDF extraction + LLM
│   └── job_api.py       # Apify job scrapers
└── .vscode/
    └── settings.json


---

## 🔧 Installation & Setup

### **Clone the repository**
```bash
git clone https://github.com/<your-username>/job-recommender.git
cd job-recommender
```

### **Create environment (uv)**
```bash
uv venv
uv sync
```

## 🔑 Environment Variables
### **Create a .env file:**
```bash
APIFY_API_TOKEN=your_token_here
```

## 🤖 LLM Setup (Ollama)

### **Ensure you have Ollama installed:**

https://ollama.com/

**Then pull the model:**
```bash
ollama pull llama3.2
```

**▶️ Run the Application**
```bash
streamlit run app.py
```

The app will launch in your browser at:
```arduino
http://localhost:8501
```

## 🧠 How It Works
### 1️⃣ Resume Upload

User uploads a PDF CV.

### 2️⃣ Text Extraction

extract_text_from_pdf() (PyMuPDF) extracts raw text.

### 3️⃣ LLM Processing

ask_llm() with Llama 3.2 generates:

Summary

Skill gaps

Future roadmap

Job search keywords

### 4️⃣ Job Scraping

fetch_linkedin_jobs()

fetch_naukri_jobs()

Both powered using Apify Actors.

### 5️⃣ Display Results

**Streamlit presents:**

Analysis

Insights

Job Recommendations
