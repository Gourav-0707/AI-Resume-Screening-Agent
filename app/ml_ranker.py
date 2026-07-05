import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load training data
df = pd.read_csv("data/training_data.csv")

X = df[[
    "similarity",
    "matched_skills",
    "missing_skills",
    "total_skills"
]]

y = df["final_score"]

# Train the model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


def predict_score(similarity,
                  matched,
                  missing,
                  total):

    prediction = model.predict([[
        similarity,
        matched,
        missing,
        total
    ]])

    return round(float(prediction[0]), 2)