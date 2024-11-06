import unittest
from modules.nlp.nlp_processor import NLPProcessor

class TestNLPProcessor(unittest.TestCase):
    def setUp(self):
        self.nlp = NLPProcessor()

    def test_saludo(self):
        response = self.nlp.process_command("Hola")
        self.assertEqual(response, "¡Hola! ¿En qué puedo ayudarte?")

    def test_control_iot(self):
        response = self.nlp.process_command("Encender luz")
        self.assertEqual(response, "Encender el dispositivo luz.")

    def test_consulta(self):
        response = self.nlp.process_command("Consultar datos")
        self.assertEqual(response, "Consulta en proceso.")

    def test_guardar(self):
        response = self.nlp.process_command("Guardar nota")
        self.assertEqual(response, "Datos guardados correctamente.")

if __name__ == "__main__":
    unittest.main()
