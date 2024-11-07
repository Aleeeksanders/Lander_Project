from modules.nlp.nlp_processor import NLPProcessor

def main():
    nlp_processor = NLPProcessor()
    print("Bienvenido al chat de prueba. Escribe 'salir' para terminar.")

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Chat terminado.")
            break

        response = nlp_processor.process_command(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
