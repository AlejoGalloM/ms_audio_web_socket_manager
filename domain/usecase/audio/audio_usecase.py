from domain.model.audio.gateway.web_socket_gateway import WebSocketGateway
from infrastructure.driven_adapter.web_socket.web_socket import WebSocket
from infrastructure.helpers.fragment.fragment_file import fragment_and_send


def send_audio(ws, encrypted_audio, gateway: WebSocketGateway = WebSocket()):
    print("Conexión WebSocket establecida.")

    file_name = input("Introduce el nombre del archivo: ")
    fragment_and_send(encrypted_audio, ws, file_name)


def transcribe_audio(ws, id_file, gateway: WebSocketGateway = WebSocket()):
    gateway.receive_message(ws, f"transcript:{id_file}")


def see_transcribe(ws, id_file, gateway: WebSocketGateway = WebSocket()):
    gateway.receive_message(ws, f"obtain:{id_file}")


def consult_status(ws, id_file, gateway: WebSocketGateway = WebSocket()):
    gateway.receive_message(ws, f"status:{id_file}")


def create_connection(gateway: WebSocketGateway = WebSocket()):
    ws = gateway.create_connection()
    return ws


def close_connection(ws):
    ws.close()


class AudioUseCase:
    pass
