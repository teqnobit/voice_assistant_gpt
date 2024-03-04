from openai import OpenAI
from dotenv import load_dotenv
from playsound import playsound
import os
# import time

from voice_to_text import generate_text_from_record

load_dotenv()
openai = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

print('Que quieres saber?')
prompt = generate_text_from_record('base')

print('Obteniendo respuesta')
response = openai.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'Eres un asistente que da respuestas cortas y concretas'
        },
        {
            'role': 'user',
            'content': prompt
        }
    ],
    # stream=True
)
# Impresion de respuesta
print(response.choices[0].message.content)

# Only with stream=True
# for chunk in response:
#     print(chunk.choices[0].delta.content or '', end='')
#     time.sleep(0.15)

# Conversion de texto a voz
print('Aclarando garganta')
speech = openai.audio.speech.create(
    model="tts-1",
    voice="echo",
    input=response.choices[0].message.content,
)
speech.stream_to_file('output.mp3')  # Sera actualizado

# Reproduccion de la respuesta
print('Entonando palabras')
playsound('output.mp3')