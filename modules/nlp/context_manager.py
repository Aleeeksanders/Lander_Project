class ContextManager:
    def __init__(self):
        # Almacenamos el contexto en un diccionario
        self.context = {}

    def update_context(self, key, value):
        """Actualiza el contexto con una nueva clave y valor"""
        self.context[key] = value

    def get_context(self, key):
        """Obtiene el valor asociado a una clave específica en el contexto"""
        return self.context.get(key)

    def clear_context(self):
        """Limpia el contexto de la conversación"""
        self.context.clear()
