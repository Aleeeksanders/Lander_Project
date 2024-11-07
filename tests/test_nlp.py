import unittest
from modules.nlp.nlp_processor import NLPProcessor

class TestNLPProcessor(unittest.TestCase):
    def setUp(self):
        self.nlp_processor = NLPProcessor()

    def test_saludo(self):
        response = self.nlp_processor.process_command("Hola")
        self.assertEqual(response, "¡Hola! ¿En qué puedo ayudarte hoy?")

    def test_control_dispositivo(self):
        response = self.nlp_processor.process_command("encender luz")
        self.assertEqual(response, "Encender el dispositivo luz.")
        # Segunda prueba para ver el contexto
        response = self.nlp_processor.process_command("apagar luz")
        self.assertEqual(response, "Ya recuerdo, quieres apagar el luz nuevamente, ¿correcto?")

    def test_consulta(self):
        response = self.nlp_processor.process_command("Consulta de clima")
        self.assertEqual(response, "Consulta en proceso.")
        # Prueba de seguimiento para el contexto
        response = self.nlp_processor.process_command("Otra consulta")
        self.assertIn("Última vez preguntaste sobre 'Consulta de clima'", response)

    def test_guardar(self):
        response = self.nlp_processor.process_command("guardar datos")
        self.assertEqual(response, "Datos guardados correctamente.")

    def test_intención_desconocida(self):
        response = self.nlp_processor.process_command("hacer algo raro")
        self.assertEqual(response, "No entendí el comando, ¿podrías reformularlo?")

if __name__ == "__main__":
    unittest.main()
