from modules.nlp.command_responses import CommandResponses
from modules.nlp.knowledge_manager import KnowledgeManager
from modules.nlp.intent_classifier import IntentClassifier
from modules.nlp.entity_recognition import EntityRecognizer
from modules.nlp.context_manager import ContextManager

class NLPProcessor:
    def __init__(self):
        self.command_responses = CommandResponses()
        self.knowledge_manager = KnowledgeManager()
        self.intent_classifier = IntentClassifier()
        self.entity_recognizer = EntityRecognizer()
        self.context_manager = ContextManager()

    def process_command(self, command):
        # Clasifica la intención del comando
        intent = self.intent_classifier.classify_intent(command)

        # Reconoce las entidades en el comando
        entities = self.entity_recognizer.recognize_entities(command)

        # Actualiza el contexto con las entidades detectadas
        if "device" in entities:
            self.context_manager.update_context("device", entities["device"])
        if "place" in entities:
            self.context_manager.update_context("place", entities["place"])

        # Obtiene el contexto en caso de que no haya una entidad específica en el comando actual
        device = entities.get("device", self.context_manager.get_context("device"))
        place = entities.get("place", self.context_manager.get_context("place"))

        # Ejecución de acuerdo con la intención
        if intent == "greeting":
            response = "¡Hola! ¿En qué puedo ayudarte?"
        elif intent == "goodbye":
            response = "Hasta luego. ¡Que tengas un buen día!"
            self.context_manager.clear_context()
        elif intent == "feedback":
            feedback = command.split(":", 1)[-1].strip()  # Asume formato "feedback: nueva respuesta"
            response = self.knowledge_manager.refine_response(command, feedback)
        elif intent == "information":
            response = "¿Podrías darme más detalles para ayudarte con la información que necesitas?"
        elif intent == "iot_command":
            if device and place:
                response = f"¿Quieres controlar el {device} en el {place}?"
            else:
                response = "No estoy seguro de qué dispositivo o lugar te refieres."
        else:
            # Si no se conoce el comando, intenta usar el aprendizaje
            response = self.knowledge_manager.get_response(command) or "No estoy seguro de cómo responder a eso. Estoy aprendiendo continuamente."

        # Aprende la nueva respuesta o ajusta la frecuencia
        self.knowledge_manager.learn_response(command, response)
        return response
