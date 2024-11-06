# command_responses.py
# Define respuestas específicas para los comandos

def obtener_respuesta(comando):
    respuestas = {
        "encender luz": "Encendiendo las luces...",
        "apagar luz": "Apagando las luces...",
        "clima": "Aquí tienes la información del clima actual...",
    }
    return respuestas.get(comando, "No entendí el comando")
