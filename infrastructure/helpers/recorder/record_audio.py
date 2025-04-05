import threading
import wave
import sounddevice as sd


def record_audio(archivo, frecuencia_muestreo=44100, canales=1):
    grabando = True
    frames = []

    def grabar():
        nonlocal grabando
        print("Grabando... Presiona 'Enter' para detener.")
        try:
            with sd.InputStream(samplerate=frecuencia_muestreo, channels=canales, dtype="int16") as stream:
                while grabando:
                    datos, _ = stream.read(1024)
                    frames.append(datos)
        except Exception as e:
            print(f"Error al grabar audio: {e}")

    hilo_grabacion = threading.Thread(target=grabar)
    hilo_grabacion.start()

    input("Presiona 'Enter' para detener la grabación.\n")
    grabando = False
    hilo_grabacion.join()

    print("Guardando grabación...")
    try:
        with wave.open(archivo, 'wb') as wf:
            wf.setnchannels(canales)
            wf.setsampwidth(2)
            wf.setframerate(frecuencia_muestreo)
            wf.writeframes(b"".join(frames))
        print(f"Grabación guardada en: {archivo}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


class RecordAudio:
    pass
