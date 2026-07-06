from app.parser import extract_text_from_pdf
from app.similarity import calculate_similarity

# Read resume
resume_text = extract_text_from_pdf("resumes/Gourav_Resume_.pdf")  # Change to your filename

# Read job description
with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_description = f.read()

# Calculate similarity
score = calculate_similarity(resume_text, job_description)

print(f"Resume Match Score: {score}%")