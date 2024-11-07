class CommandResponses:
    def get_response(self, intent, command, context):
        """
        Retorna una respuesta en función de la intención identificada y el contexto.
        """
        if intent == "control_dispositivo":
            return self.control_device_response(command, context)
        elif intent == "consulta":
            return self.consult_response(command, context)
        elif intent == "guardar":
            return "Datos guardados correctamente."
        elif intent == "saludo":
            return "¡Hola! ¿En qué puedo ayudarte hoy?"
        else:
            return "No entendí el comando, ¿podrías reformularlo?"

    def control_device_response(self, command, context):
        """
        Genera una respuesta específica para comandos de control de dispositivos.
        """
        action = "encender" if "encender" in command else "apagar"
        device = command.replace(action, "").strip()
        
        # Respuesta personalizada según el contexto.
        if 'last_device' in context and context['last_device'] == device:
            return f"Ya recuerdo, quieres {action} el {device} nuevamente, ¿correcto?"
        
        return f"{action.capitalize()} el dispositivo {device}."

    def consult_response(self, command, context):
        """
        Genera una respuesta para consultas, considerando el contexto de consultas anteriores.
        """
        if 'last_query' in context:
            return f"Última vez preguntaste sobre '{context['last_query']}'. Ahora estás preguntando sobre '{command}', ¿verdad?"
        
        return "Consulta en proceso."
