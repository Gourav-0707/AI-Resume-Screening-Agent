import os
import pandas as pd

from app.parser import extract_text_from_pdf
from app.similarity import calculate_similarity
from app.utils import extract_skills
from app.skill_match import compare_skills
from app.ml_ranker import predict_score
from app.ats_score import calculate_ats_score
from app.experience import extract_experience
from app.education import extract_education


def rank_resumes(resume_folder, job_description):

    results = []

    job_skills = extract_skills(job_description)

    for file in os.listdir(resume_folder):

        if file.endswith(".pdf"):

            path = os.path.join(resume_folder, file)

            resume_text = extract_text_from_pdf(path)

            similarity_score = calculate_similarity(
                resume_text,
                job_description
            )

            skills = extract_skills(resume_text)

            matched_skills, missing_skills = compare_skills(
                resume_text,
                job_description
            )

            matched_count = len(matched_skills)
            missing_count = len(missing_skills)
            total_skills = len(job_skills)

            ats_score = calculate_ats_score(
                similarity_score,
                matched_count,
                total_skills
            )

            experience = extract_experience(resume_text)

            education = extract_education(resume_text)

            ml_score = predict_score(
                similarity=similarity_score,
                matched=matched_count,
                missing=missing_count,
                total=total_skills
            )

            if ml_score >= 85:
                recommendation = "Highly Recommended"
            elif ml_score >= 70:
                recommendation = "Recommended"
            else:
                recommendation = "Needs Improvement"

            results.append({
                "Resume": file,
                "Similarity Score": similarity_score,
                "ATS Score": ats_score,
                "ML Candidate Score": ml_score,
                "Experience (Years)": experience,
                "Education": education,
                "Skills Found": ", ".join(skills),
                "Matched Skills": ", ".join(matched_skills),
                "Missing Skills": ", ".join(missing_skills),
                "Recommendation": recommendation
            })

    results = sorted(
        results,
        key=lambda x: x["ML Candidate Score"],
        reverse=True
    )

    return results


def save_results(results):

    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(results)

    df.to_csv(
        "output/results.csv",
        index=False
    )

    print("Results saved to output/results.csv")