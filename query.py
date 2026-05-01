from vector_store import create_index, search
from llm import generate_answer

def run_query():
    index, docs = create_index()

    while True:
        query = input("\nAsk something (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        results = search(query, index, docs)
        context = "\n\n".join(results)

        answer = generate_answer(context, query)

        print("\nAnswer:\n", answer)

if __name__ == "__main__":
    run_query()