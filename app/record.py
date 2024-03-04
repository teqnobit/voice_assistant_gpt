import pyaudio
import wave
import audioop

# Configuración de parámetros de grabación
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 22050
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio_grabado.wav"
THRESHOLD = 1500  # Umbral de volumen para determinar si hay sonido

# Inicializar el objeto PyAudio
audio = pyaudio.PyAudio()

# Abrir el stream de audio para la grabación
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Grabando audio...")

# Lista para almacenar los fragmentos de audio grabados
frames = []

##### Prueba de record infinito #####
# # Grabar audio en fragmentos
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK, exception_on_overflow=False)
#     frames.append(data)
# Grabar audio en fragmentos
cuenta = 0
while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    frames.append(data)

    rms = audioop.rms(data, 2)

    if rms < THRESHOLD:
        cuenta += 1 
    else:
        cuenta = 0

    if cuenta > RATE / CHUNK * 2:
        break


print("¡Grabación finalizada!")

# Detener y cerrar el stream de audio
stream.stop_stream()
stream.close()
audio.terminate()

# Guardar el audio grabado en un archivo WAV
wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b''.join(frames))
wave_file.close()

print("Audio grabado guardado en", WAVE_OUTPUT_FILENAME)