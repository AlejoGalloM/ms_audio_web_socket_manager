from domain.model.audio.gateway.web_socket_gateway import WebSocketGateway
from infrastructure.driven_adapter.web_socket.config.ws_contants import WS_TRANSCRIBE

import websocket


class WebSocket(WebSocketGateway):
    def create_connection(self):
        try:
            ws = websocket.create_connection(WS_TRANSCRIBE)
            print("Conexión WebSocket establecida.")
            return ws
        except Exception as e:
            print(f"Error al establecer la conexión WebSocket: {e}")
            return None

    def send_message(self, ws, message):
        try:
            ws.send(message)
            print("Audio enviado a través de WebSocket.")
        except Exception as e:
            print(f"Error al establecer la conexión WebSocket: {e}")
            return None

    def receive_message(self, ws, message):
        try:
            ws.send(message)
            response = ws.recv()
            print(f"Respuesta del WebSocket: {response}")
            return response
        except Exception as e:
            print(f"Error al establecer la conexión WebSocket: {e}")
            return None

    def close_connection(self, ws):
        try:
            ws.close()
            print("Conexión WebSocket cerrada.")
        except Exception as e:
            print(f"Error al establecer la conexión WebSocket: {e}")
            return None

    def listen_ws(self, ws):
        try:
            response = ws.recv()
            print(f"Respuesta del WebSocket: {response}")
            return response
        except Exception as e:
            print(f"Error al establecer la conexión WebSocket: {e}")
            return None
