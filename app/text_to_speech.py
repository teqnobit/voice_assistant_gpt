from openai import OpenAI
from dotenv import load_dotenv
from playsound import playsound
import os

load_dotenv()
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Andrés Manuel López Obrador.",
)

response.stream_to_file('output.mp3')
playsound('./output.mp3')