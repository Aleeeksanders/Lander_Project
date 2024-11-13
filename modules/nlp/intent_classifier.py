import re

class IntentClassifier:
    def __init__(self):
        # Definimos patrones para distintas intenciones
        self.intents = {
            "greeting": r"\b(hola|buenas|hey|saludos)\b",
            "goodbye": r"\b(adios|hasta luego|nos vemos)\b",
            "information": r"\b(quien|que|cuando|donde|por que|cuanto|como)\b",
            "iot_command": r"\b(encender|apagar|activar|desactivar)\b"
        }

    def classify_intent(self, text):
        # Recorremos cada intención y revisamos si el texto coincide con el patrón
        for intent, pattern in self.intents.items():
            if re.search(pattern, text, re.IGNORECASE):
                return intent
        return "unknown"  # Si no coincide, lo clasificamos como desconocido
