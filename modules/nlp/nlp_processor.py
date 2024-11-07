class NLPProcessor:
    def __init__(self):
        pass

    def process_command(self, command):
        # Simulación de respuestas basadas en palabras clave
        if "hola" in command.lower():
            return "¡Hola! ¿En qué puedo ayudarte?"
        elif "encender" in command.lower():
            return "Encender el dispositivo luz."
        elif "apagar" in command.lower():
            return "Apagar el dispositivo luz."
        elif "guardar" in command.lower():
            return "Datos guardados correctamente."
        elif "consulta" in command.lower():
            return "Consulta en proceso."
        else:
            return "Intención desconocida. Por favor, intenta de nuevo."
