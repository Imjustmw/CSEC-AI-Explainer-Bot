# CSEC Math Explainer Bot

A lightweight AI-powered math assistant designed to help Caribbean students prepare for their **CXC CSEC Mathematics** exams — even in low-internet environments. Built to simulate how an intelligent tutor would retrieve and explain concepts, this tool leverages vector search and sentence embeddings to match a student’s question with the best possible explanation from a small offline knowledge base.

---

## Why I Built This & Why I'm Proud of It

I built this project to solve a real problem in the Caribbean: **limited access to smart, adaptive educational tools**. Many students don’t have fast or stable internet, but still need support to prepare for critical exams like CSEC.

This app shows that you don't need a massive model or cloud infrastructure to create AI-like behavior. Using **local embeddings** and a clean UI, this tool lets students type a question in plain language and receive the most relevant explanation — even offline.

I'm proud of it because it blends my passions for **AI, education, and accessibility** in a real-world way. It was built completely outside of class, and I challenged myself to go from idea to working prototype in just **under an hour**. That urgency pushed me to keep things lean, efficient, and focused — a mindset I bring to real-world engineering problems.

---

## Why This Project Matters (For Internships)

This isn’t just a side project — it’s a real demonstration of how I approach problems:

- I built it in **under 1 hour**, showing that I can ship fast while thinking clearly under time constraints.
- It solves a **real-world problem** using AI, not just for hype but for accessibility.
- It showcases my ability to move across the stack: from **ML to backend to frontend** — and package it cleanly.

If I could do this in an hour, imagine what I could build with a team and a full day.

---

## Project Overview

- **Frontend:** Simple HTML + JavaScript
- **Backend:** Python + Flask
- **AI/ML Component:** `sentence-transformers` (MiniLM) for semantic similarity
- **Data:** JSON-based CSEC math concept/explanation dataset

---

## Demo Video

Watch a short demo:
[Watch the demo on Google Drive](https://drive.google.com/file/d/1xRCm3W0n8ega0iHN-s2-tW3sKXDLPYaa/view?usp=sharing)
---

## Try It Yourself

### Requirements

- Python 3.7+
- pip

### Installation

1. Clone this repo:

```bash
git clone https://github.com/your-username/csec-explainer.git
cd csec-explainer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
flask --app app --debug run
```

4. Open your browser at:
```bash
http://localhost:5000
```

---

## Example Usage

1. Ask:
`What is a right angle triangle?`

2. Output:
```bash
Closest match: What is the Pythagorean Theorem?
Answer: In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.
```

If the system doesn't find a match, it says:
`"I don’t know this yet. Try asking in a different way or check your textbook."`

---

## How it Works

- Each concept in explainers.json is embedded using a small, local language model.
- When a student types a question, the tool computes semantic similarity and returns the closest match.
- If the similarity score is too low, it gives a helpful fallback message.
- All logic is handled client-side + locally — no internet needed after setup.

---

## File Structure
```bash
csec-vector-search/
├── app.py
├── explainers.json
├── utils.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
└── README.md
```

---

## Tech Stack

- Python
- Flask
- Sentence Transformers (MiniLM)
- scikit-learn (for cosine similarity)
- HTML/CSS/JS