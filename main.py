from utils import load_data, get_most_similar_explanation

def main():
    print("Ask me any CSEC Math question/Type 'exit' to quit\n")

    data, embeddings, model = load_data("explainers.json")

    while True:
        user_input = input("> ")
        if user_input.lower().strip() == "exit":
            break

        result = get_most_similar_explanation(user_input, data, embeddings, model)
        print(f"\nClosest match: {result['question']}")
        print(f"\nAnswer: {result['answer']}")

if __name__ == "__main__":
    main()
