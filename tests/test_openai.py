import openai

# Reemplaza 'tu_clave_api_aquí' con tu clave API real
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Cambia a 'gpt-4' si tienes acceso
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].text.strip())
