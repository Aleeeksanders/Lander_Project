import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self, language="es-ES"):
        self.recognizer = sr.Recognizer()
        self.language = language

    def listen(self):
        """Escucha el audio desde el micrófono y convierte a texto."""
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = self.recognizer.listen(source)
            try:
                print("Reconociendo...")
                text = self.recognizer.recognize_google(audio, language=self.language)
                print(f"Texto reconocido: {text}")
                return text
            except sr.UnknownValueError:
                print("No se entendió el audio.")
                return ""
            except sr.RequestError:
                print("Error al comunicarse con el servicio de reconocimiento.")
                return ""

# Ejemplo de uso
if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    command = recognizer.listen()
    print(f"Comando recibido: {command}")
