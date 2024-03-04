import whisper
from record import start_record

def generate_text_from_record(model='small', language='es'):
    # Start recording
    start_record()

    # Use to download models
    # model = whisper.load_model(name='small', download_root='./models/') 

    # transcribe speech to text
    print('Procesando audio')
    model = whisper.load_model(f'./models/{model}.pt')
    result = model.transcribe('./audio_grabado.wav', fp16=False, language=language)

    # Result
    return result['text']

# print(generate_text_from_record())