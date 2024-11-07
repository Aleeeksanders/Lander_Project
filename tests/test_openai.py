import openai

# Reemplaza 'tu_clave_api_aquí' con tu clave API real
openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Cambia a 'gpt-4' si tienes acceso
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].text.strip())
