from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resume_text, job_description):
    # Generate embeddings
    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_description])

    # Compute cosine similarity
    similarity = cosine_similarity(resume_embedding, job_embedding)

    return round(float(similarity[0][0]) * 100, 2)