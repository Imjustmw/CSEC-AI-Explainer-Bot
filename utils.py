import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = [entry['question'] for entry in data]
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(questions)

    return data, embeddings, model


def get_most_similar_explanation(user_input, data, embeddings, model):
    user_embedding = model.encode([user_input])
    similarities = cosine_similarity(user_embedding, embeddings)[0]
    best_idx = int(np.argmax(similarities))
    return data[best_idx]