from app.ml_ranker import predict_score

score = predict_score(
    similarity=82,
    matched=8,
    missing=2,
    total=10
)

print(score)