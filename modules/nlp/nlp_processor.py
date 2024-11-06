class NLPProcessor:
    def __init__(self):
        # Diccionario de intenciones básicas con palabras clave
        self.intentions = {
            "guardar": ["guardar", "almacenar", "recordar"],
            "controlar_dispositivo": ["encender", "apagar", "activar", "desactivar"],
            "pregunta": ["qué", "quién", "cómo", "dónde", "por qué"],
            # Puedes añadir más intenciones según sea necesario
        }

    def process_command(self, command):
        # Convierte el comando a minúsculas para un análisis básico
        command = command.lower()

        # Detectar intención a partir del comando
        for intent, keywords in self.intentions.items():
            if any(keyword in command for keyword in keywords):
                return intent

        # Si no encuentra ninguna intención específica
        return "intención_desconocida"
