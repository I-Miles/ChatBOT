import os
import google.generativeai as genai

api_key = ''
os.environ["API_KEY"] = api_key
genai.configure(api_key=os.environ["API_KEY"])

def chatbot():
    print("Bem-vindo ao Rego.AI")
    print("Digite oque deseja saber que o Rego ira te respoder.")
    print("Para sair, digite 'sair'.\n")

    while True:
        user_input = input("Você: ")

        if user_input.lower() == 'sair':
            print("Saindo do chat. Até logo!")
            break

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            print(response.text)

        except Exception as e:
            print(f"Ocorreu um erro ao chamar a API: {e}")
chatbot()