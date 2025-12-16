from app.recommender import AssessmentRecommender


def test_recommendations():
    engine = AssessmentRecommender("data/shl_catalog.csv")
    results = engine.recommend("data analyst sql python")

    assert len(results) > 0
    assert "name" in results[0]
