# AI Resume Screening Agent

## Overview

The AI Resume Screening Agent is a FastAPI-based application that automates the resume screening process. It extracts text from PDF resumes, compares them with a job description using NLP techniques, calculates ATS scores, predicts candidate rankings using a Random Forest Machine Learning model, and recommends suitable candidates.

---

## Features

- Upload PDF resumes
- Resume text extraction
- Skill extraction
- Semantic similarity using Sentence Transformers
- ATS score calculation
- Candidate ranking using Random Forest
- Experience extraction
- Education extraction
- Resume recommendation
- CSV export of ranked candidates
- FastAPI REST API
- Interactive Swagger UI

---

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- Scikit-learn
- Random Forest
- PyMuPDF
- Pandas
- NumPy

---

## Project Structure

```
ResumeScreeningAgent
│
├── app
│   ├── main.py
│   ├── ranker.py
│   ├── parser.py
│   ├── similarity.py
│   ├── skill_match.py
│   ├── ml_ranker.py
│   ├── ats_score.py
│   ├── education.py
│   ├── experience.py
│   ├── utils.py
│   └── __init__.py
│
├── data
│   ├── job_description.txt
│   └── training_data.csv
│
├── resumes
├── output
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Gourav-0707/AI-Resume-Screening-Agent.git
```

### Navigate to Project

```bash
cd AI-Resume-Screening-Agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home API |
| GET | /rank | Rank all resumes |
| POST | /upload | Upload a PDF resume |

---

## Workflow

```
PDF Resume
      │
      ▼
Resume Parser
      │
      ▼
Skill Extraction
      │
      ▼
Sentence Transformer
      │
      ▼
Semantic Similarity
      │
      ▼
ATS Score Calculation
      │
      ▼
Random Forest ML Model
      │
      ▼
Candidate Ranking
      │
      ▼
Recommendation
      │
      ▼
CSV Export + FastAPI Response
```

---

## Sample Output

| Resume | Similarity | ATS | ML Score | Recommendation |
|----------|-----------|------|-----------|----------------|
| Resume1.pdf | 82.5 | 85.4 | 88.7 | Highly Recommended |
| Resume2.pdf | 71.2 | 73.5 | 76.9 | Recommended |

---
## Swagger UI

![Swagger UI](images/swagger.png)

---

## Resume Ranking API

![Rank API](images/rank_result.png)

---

## Future Improvements

- OCR support for scanned resumes
- LLM-based resume analysis
- Recruiter dashboard
- Email notifications
- Database integration
- Authentication
- Resume analytics dashboard

---

## Author

**Gourav Raikar**

AI Engineer | Python | Machine Learning | FastAPI 