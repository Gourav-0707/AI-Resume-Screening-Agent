from fastapi import FastAPI, UploadFile, File
from app.ranker import rank_resumes, save_results
import shutil
import os

app = FastAPI(
    title="AI Resume Screening Agent",
    description="""
AI-powered Resume Screening System

Features:
- Resume Upload API
- Resume Parsing
- Skill Extraction
- Semantic Similarity using Sentence Transformers
- ATS Score Calculation
- Machine Learning Candidate Ranking (Random Forest)
- Recommendation System
- Resume Ranking
""",
    version="1.0.0"
)


@app.get("/", tags=["Home"])
def home():
    return {
        "Project": "AI Resume Screening Agent",
        "Version": "1.0.0",
        "Developer": "Gourav Raikar",
        "Status": "Running Successfully"
    }


@app.get("/rank", tags=["Resume Ranking"])
def rank_resumes_api():
    """
    Rank all resumes available in the resumes folder.
    """

    with open("data/job_description.txt", "r", encoding="utf-8") as file:
        job_description = file.read()

    results = rank_resumes("resumes", job_description)

    # Save latest rankings to CSV
    save_results(results)

    return {
        "Success": True,
        "Total Candidates": len(results),
        "Rankings": results
    }


@app.post("/upload", tags=["Resume Upload"])
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload a PDF resume.
    """

    if not file.filename.lower().endswith(".pdf"):
        return {
            "success": False,
            "message": "Only PDF files are allowed."
        }

    os.makedirs("resumes", exist_ok=True)

    file_path = os.path.join("resumes", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "success": True,
        "message": "Resume uploaded successfully.",
        "filename": file.filename
    }