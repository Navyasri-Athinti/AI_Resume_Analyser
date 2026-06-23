# 🤖 AI Resume Analyzer

🔗 Live Demo: https://airesumeanalyser-d3s8bt3kzup6kx7jeqszsn.streamlit.app/

An AI-powered Resume Analyzer built using Python, Streamlit, and Google Gemini AI that helps users evaluate resumes, identify missing skills, compare resumes with job descriptions, and receive AI-generated improvement suggestions.

This project was created to make resume screening smarter, faster, and more interactive using Generative AI and NLP techniques.

---

# ✨ Features

* 📄 Upload Resume in PDF format
* 🧠 AI-powered resume analysis using Google Gemini AI
* 🎯 Compare resume with job descriptions
* 📊 Identify strengths and weaknesses in the resume
* 🛠️ Suggest missing skills and improvements
* 📚 Recommend courses and learning areas
* 🔍 Extract text from both normal and scanned PDFs
* ⚡ Simple and interactive Streamlit interface

---

# 🧠 How It Works

1. User uploads a resume PDF
2. The system extracts text from the resume
3. If the PDF is image-based/scanned, OCR is used for text extraction
4. The extracted content is sent to Gemini AI
5. Gemini analyzes the resume and provides:

   * Resume evaluation
   * Skill analysis
   * Improvement suggestions
   * Job-role matching feedback

---

# 🛠️ Tech Stack

## Languages & Frameworks

* Python
* Streamlit

## AI & NLP

* Google Gemini AI
* Prompt Engineering

## Libraries Used

* pdfplumber
* pytesseract
* pdf2image
* python-dotenv

---

# 📂 Project Structure

```bash
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── AI_Resume_Analyzer.ipynb
└── README.md
```

---

# 🚀 Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Create a `.env` File

Create a file named `.env` and add your Gemini API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

You can generate your API key from:
[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

# 🎯 Future Improvements

* ATS Score Calculation
* Resume Ranking System
* Multi-language Resume Support
* PDF Report Generation
* Voice-based Resume Review
* Resume Templates Recommendation
* Job Recommendation System

---

# 💡 What I Learned

Through this project, I learned:

* Working with Generative AI APIs
* Resume parsing and text extraction
* OCR for scanned documents
* Prompt engineering techniques
* Streamlit application development
* Building AI-powered real-world applications
* Handling user-uploaded files securely

---

# 👩‍💻 Developed By

**Navyasri**

Built as part of my AI/ML learning journey.

---
