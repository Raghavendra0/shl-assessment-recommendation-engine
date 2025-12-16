import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class AssessmentRecommender:
    def __init__(self, data_path: str):
        self.df = pd.read_csv(data_path)

        self.df["combined_text"] = (
            self.df["skills"] + " " + self.df["job_roles"]
        )

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.df["combined_text"]
        )

    def recommend(self, query: str, top_k: int = 3):
        query_vector = self.vectorizer.transform([query])
        similarity_scores = cosine_similarity(
            query_vector, self.tfidf_matrix
        )[0]

        self.df["match_score"] = similarity_scores

        recommendations = (
            self.df.sort_values("match_score", ascending=False)
            .head(top_k)
            .drop(columns=["combined_text"])
        )

        return recommendations.to_dict(orient="records")
