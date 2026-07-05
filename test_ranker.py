from app.ranker import rank_resumes, save_results

with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_description = f.read()

results = rank_resumes("resumes", job_description)

for i, resume in enumerate(results, start=1):
    print(f"{i}. {resume['Resume']} - {resume['Match Score']}%")

save_results(results)