# SHL Assessment Recommendation Engine

## 📌 Overview
This project implements a machine learning–based **Assessment Recommendation Engine** that suggests suitable SHL-style assessments based on job role and required skills.  
The solution demonstrates how an intelligent system can map hiring requirements to relevant assessments using natural language processing (NLP).

---

## 🎯 Problem Statement
Given a hiring requirement (job role and skills), recommend the most relevant assessments from an assessment catalogue in a scalable, explainable, and reproducible way.

---

## 🧠 Approach & Methodology

1. **Data Representation**
   - Each assessment contains associated skills and job roles.
   - Skills and roles are combined into a single textual representation.

2. **Text Vectorization**
   - TF-IDF (Term Frequency–Inverse Document Frequency) is used to convert text into numerical vectors.

3. **Similarity Matching**
   - Cosine similarity measures relevance between user input and assessment vectors.

4. **Ranking**
   - Assessments are ranked by similarity score and top recommendations are returned.

This approach is:
- Lightweight
- Interpretable
- Easily extendable to larger catalogues

---

Swagger UI

The application will run on http://127.0.0.1:8000/docs