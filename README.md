# 🤖 AI Resume Analyzer

> An AI-powered application that analyzes a resume against a job description using Generative AI and provides actionable career insights.

## 🚀 Overview

AI Resume Analyzer helps candidates understand how well their resume matches a specific job description.

Users can upload their resume, provide a job description, and receive an AI-generated analysis covering skills, strengths, missing skills, experience match, education match, and recommendations.

## ✨ Features

- 📄 Upload Resume in PDF format
- 💼 Paste a Job Description
- 🤖 AI-powered Resume Analysis
- 🎯 Resume & Job Description Matching
- 💪 Identify Candidate Strengths
- ❌ Identify Missing Skills
- 💡 Personalized Recommendations
- 💼 Experience Match Analysis
- 🎓 Education Match Analysis
- ⚡ Interactive Streamlit Interface

## 🖥️ Application Preview
https://rapunzel-resume-analyzer.streamlit.app/
### Resume & Job Description

Upload your resume and enter the target job description.

![Resume Upload and Job Description](screenshots/input.png)

### AI Analysis

The application identifies missing skills and highlights the candidate's strengths.

![Missing Skills and Strengths](screenshots/analysis.png)

### Experience & Education Match

The AI evaluates the candidate's experience and education against the job requirements.

![Experience and Education Match](screenshots/match.png)

## 🧠 How It Works

```text
Resume PDF
    │
    ▼
Text Extraction
    │
    ▼
Job Description
    │
    ▼
Gemini AI
    │
    ▼
Resume Analysis
    │
    ├── Strengths
    ├── Missing Skills
    ├── Recommendations
    ├── Experience Match
    └── Education Match


🚀 Installation & Setup

Follow these steps to run the AI Resume Analyzer locally.

Prerequisites

Make sure you have the following installed:

- Python 3.10+
- Git
- pip

1. Clone the Repository

git clone https://github.com/realshafique/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

2. Create a Virtual Environment

python -m venv venv

Activate the virtual environment:

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a ".env" file in the project root:

API_KEY=your_api_key_here

Replace "your_api_key_here" with your actual API key.

«⚠️ Never commit your ".env" file or API keys to GitHub.»

5. Start the Backend

If the project uses FastAPI:

uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

FastAPI documentation:

http://127.0.0.1:8000/docs

6. Start the Frontend

Open another terminal, activate the virtual environment, and run:

streamlit run app.py

The Streamlit application will open in your browser.

📁 Project Structure

AI-Resume-Analyzer/
│
├── backend/
├── frontend/
├── models/
├── requirements.txt
├── .env
├── .gitignore
└── README.md

«The exact folder structure may vary depending on the current project version.»

🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- NLP
- Machine Learning
- Generative AI
- REST API
