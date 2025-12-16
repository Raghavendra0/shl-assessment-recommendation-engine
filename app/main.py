from fastapi import FastAPI
from app.recommender import AssessmentRecommender
from app.schemas import RecommendationRequest

app = FastAPI(
    title="SHL Assessment Recommendation Engine",
    description="Recommends SHL assessments based on job role and skills",
    version="1.0"
)

engine = AssessmentRecommender("data/shl_catalog.csv")


@app.post("/recommend")
def recommend_assessment(request: RecommendationRequest):
    return engine.recommend(request.query)
