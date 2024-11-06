import unittest
from modules.speech.text_to_speech import TextToSpeech

class TestTextToSpeech(unittest.TestCase):
    def setUp(self):
        # Configura el TTS con Polly antes de cada prueba
        self.tts = TextToSpeech(voice_id="Lupe", language_code="es-ES")

    def test_speak(self):
        """Prueba que el método speak funcione sin errores."""
        try:
            self.tts.speak("Esta es una prueba de reproducción en tiempo real desde Amazon Polly.")
            print("Reproducción en tiempo real completada exitosamente.")
        except Exception as e:
            self.fail(f"Error al reproducir en tiempo real con Polly: {str(e)}")

if __name__ == "__main__":
    unittest.main()
