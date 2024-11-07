import sys
import os

# Agrega la ruta del proyecto a sys.path para que se puedan importar los módulos correctamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.nlp.nlp_processor import NLPProcessor

def main():
    nlp_processor = NLPProcessor()
    print("Bienvenido al chat. Escribe 'salir' para terminar.")

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            break
        response = nlp_processor.process_command(user_input)
        print("IA:", response)

if __name__ == "__main__":
    main()
