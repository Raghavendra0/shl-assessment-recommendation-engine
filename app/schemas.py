from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    query: str
