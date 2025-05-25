from utils import load_data, get_most_similar_explanation
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

data, embeddings, model = load_data("explainers.json")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("question", "")
    result = get_most_similar_explanation(user_input, data, embeddings, model)
    return jsonify(result)

# def main():
#     print("Ask me any CSEC Math question/Type 'exit' to quit\n")

#     data, embeddings, model = load_data("explainers.json")

#     while True:
#         user_input = input("> ")
#         if user_input.lower().strip() == "exit":
#             break

#         result = get_most_similar_explanation(user_input, data, embeddings, model)
#         print(f"\nClosest match: {result['question']}")
#         print(f"\nAnswer: {result['answer']}")

if __name__ == "__main__":
    #main()
    app.run(debug=True)
