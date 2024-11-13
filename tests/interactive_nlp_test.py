import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.nlp.nlp_processor import NLPProcessor

def main():
    nlp_processor = NLPProcessor()
    print("Bienvenido al chat. Escribe 'salir' para terminar.")

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            print("Saliendo del chat. ¡Hasta luego!")
            break
        
        response = nlp_processor.process_command(user_input)
        print("Lander:", response)

if __name__ == "__main__":
    main()
