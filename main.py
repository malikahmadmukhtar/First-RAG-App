import google.generativeai as genai


def load_context(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def initialize_gemini(api_key):
    genai.configure(api_key=api_key)


def ask_gemini(question, context):
    prompt = f"""
    Context:
    {context}
    You are an AI helper chatbot for Daraz app and you should answer the user's queries based on the given context only
    but you should talk to the user in a friendly way and guide them to daraz support if you dont find answers in your 
    context dont give any extra info about yourself or what you can or cannot do
    {question}
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    API_KEY = "AIzaSyDTOQBCbY0QknSkerqiHcjhCKPsrC6USzU"  
    FILE_PATH = "context.txt"

    initialize_gemini(API_KEY)
    context = load_context(FILE_PATH)

    while True:
        question = input("Ask a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break

        answer = ask_gemini(question, context)
        print("Answer:", answer)
