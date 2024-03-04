from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()
openai = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

response = openai.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'Eres un asistente que da respuestas cortas y concretas'
        },
        {
            'role': 'user',
            'content': '¿Quién descubrió América?'
        }
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content or '', end='')
    time.sleep(0.15)