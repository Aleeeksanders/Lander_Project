import json
import boto3
from modules.iot_control.device_manager import DeviceManager
from modules.nlp.nlp_processor import NLPProcessor
from modules.speech.text_to_speech import TextToSpeech
from modules.speech.speech_recognizer import SpeechRecognizer

# Inicialización de DynamoDB y módulos
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LanderData')

device_manager = DeviceManager()
nlp_processor = NLPProcessor()
text_to_speech = TextToSpeech(voice_id="Lucia", language_code="es-ES")
speech_recognizer = SpeechRecognizer(language="es-ES")

def lambda_handler(event, context):
    # Escucha el comando de voz
    command = speech_recognizer.listen()
    
    if not command:
        response_text = "No se entendió el comando, por favor intenta nuevamente."
        text_to_speech.speak(response_text)
        return {
            'statusCode': 200,
            'body': json.dumps(response_text)
        }
    
    # Procesa el comando con NLP
    response = nlp_processor.process_command(command)

    # Ejemplo de guardar en DynamoDB
    if "guardar" in command:
        table.put_item(Item={
            'userID': 'default_user',
            'command': command,
            'response': response,
            'timestamp': str(context.aws_request_id)
        })
        response_text = "Datos guardados en DynamoDB."
        text_to_speech.speak(response_text)
        return {
            'statusCode': 200,
            'body': json.dumps(response_text)
        }
    
    # Control de dispositivos IoT
    elif "encender" in command or "apagar" in command:
        device_action = command.split()[0]
        device_name = " ".join(command.split()[1:])
        result = device_manager.control_device(device_name, device_action)
        text_to_speech.speak(result)
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }

    # Respuesta por defecto
    response_text = f"Comando recibido: {command} - Respuesta: {response}"
    text_to_speech.speak(response_text)
    return {
        'statusCode': 200,
        'body': json.dumps(response_text)
    }
