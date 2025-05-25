import json, re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation (Callback from the technical questions)
    return text

def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = [preprocess(entry['question']) for entry in data]
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(questions)

    return data, embeddings, model

def get_most_similar_explanation(user_input, data, embeddings, model, threshold=0.4):
    user_input_clean = preprocess(user_input)
    user_embedding = model.encode([user_input_clean])
    similarities = cosine_similarity(user_embedding, embeddings)[0]
    best_idx = int(np.argmax(similarities))
    best_score = similarities[best_idx]

    if best_score < threshold:
        return {
            "question": None,
            "answer": "I don't know this yet. Try asking in a different way or check your textbook. Apologies."
        }

    return data[best_idx]