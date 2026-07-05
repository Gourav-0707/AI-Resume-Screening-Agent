from app.utils import extract_skills

def compare_skills(resume_text, job_description):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    matched = list(resume_skills.intersection(job_skills))
    missing = list(job_skills.difference(resume_skills))

    return sorted(matched), sorted(missing)