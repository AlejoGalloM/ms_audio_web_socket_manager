from infrastructure.helpers.recorder.record_audio import record_audio
from infrastructure.helpers.encode.encode_and_zip import encode_and_zip
from domain.usecase.audio.audio_usecase import send_audio, transcribe_audio, consult_status, see_transcribe, \
    create_connection, close_connection


def recorder_audio(ws):
    print("Has elegido grabar audio y enviarlo al servidor.")
    archivo_audio = "grabacion.wav"
    record_audio(archivo_audio)
    encrypted_audio = encode_and_zip(archivo_audio)
    if encrypted_audio:
        send_audio(ws, encrypted_audio)


def transcript_audio(ws):
    print("Has elegido enviar un archivo existente para transcripción.")
    id_file = input("Introduce el nombre del archivo: ")
    transcribe_audio(ws, id_file)


def obtain_status(ws):
    print("Has elegido consultar el estado de la transcripción.")
    id_file = input("Introduce el nombre del archivo: ")
    consult_status(ws, id_file)


def get_transcribe(ws):
    print("Has elegido ver la transcripción.")
    id_file = input("Introduce el nombre del archivo: ")
    see_transcribe(ws, id_file)


def salir(ws):
    print("Saliendo del programa...")
    close_connection(ws)
    return True


opciones = {
    '1': recorder_audio,
    '2': transcript_audio,
    '3': obtain_status,
    '4': get_transcribe,
    '5': salir
}


def console():
    ws = create_connection()
    while True:
        print("\nOpciones:")
        print("1. Grabar audio y enviarlo al servidor")
        print("2. Enviar archivo existente para transcripción")
        print("3. Consultar estado de la transcripción")
        print("4. Ver transcripción")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ")

        accion = opciones.get(opcion)
        if accion:
            if accion(ws):
                break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
