import boto3
import pyaudio
from contextlib import closing
from config.settings import VOICE_ID, LANGUAGE_CODE

class TextToSpeech:
    def __init__(self, voice_id="Salli", language_code="en-US"):
        self.polly_client = boto3.client('polly')
        self.voice_id = voice_id
        self.language_code = language_code

    def speak(self, text):
        # Envolver el texto en SSML con ajustes para un tono juvenil, suave y expresivo
        ssml_text = f"""
        <speak>
            <prosody rate="135%" pitch="+5%" volume="x-soft">
                <emphasis level="moderate">{text}</emphasis>
            </prosody>
        </speak>
        """

        try:
            # Solicitar el audio a Polly usando SSML y el motor NTTS
            response = self.polly_client.synthesize_speech(
                VoiceId=self.voice_id,
                OutputFormat="pcm",
                Text=ssml_text,
                TextType="ssml",  # Especificamos que estamos usando SSML
                LanguageCode=self.language_code,
                Engine="neural"  # Activar NTTS
            )
        except self.polly_client.exceptions.InvalidSsmlException as e:
            print("Error en el formato SSML:", e)
            return
        except Exception as e:
            print("Error en la síntesis de voz:", e)
            return

        # Configuración para pyaudio
        audio_stream = pyaudio.PyAudio()
        stream = audio_stream.open(format=audio_stream.get_format_from_width(width=2),
                                   channels=1,
                                   rate=16000,
                                   output=True)

        # Reproduce el flujo de datos en tiempo real
        if "AudioStream" in response:
            with closing(response["AudioStream"]) as audio_stream_data:
                while True:
                    data = audio_stream_data.read(1024)
                    if len(data) == 0:
                        break
                    stream.write(data)

        # Cierra el flujo de audio
        stream.stop_stream()
        stream.close()
        audio_stream.terminate()
