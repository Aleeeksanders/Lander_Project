import re

class EntityRecognizer:
    def __init__(self):
        # Definimos patrones básicos para las entidades
        self.entities_patterns = {
            "device": r"\b(luz|ventilador|cámara|puerta|termómetro)\b",
            "person": r"\b(Alex|Juan|Sofia|Carla)\b",
            "place": r"\b(sala|cocina|baño|garaje)\b"
        }

    def recognize_entities(self, text):
        entities = {}
        # Recorremos cada entidad y revisamos si el texto contiene el patrón
        for entity, pattern in self.entities_patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                entities[entity] = match.group(0)
        return entities
