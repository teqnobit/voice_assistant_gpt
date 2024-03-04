import whisper

# model = whisper.load_model(name='small', download_root='./models/')  # Use to download models
model = whisper.load_model('./models/small.pt')
result = model.transcribe('./audio_grabado.wav', fp16=False)

print(result['text'])