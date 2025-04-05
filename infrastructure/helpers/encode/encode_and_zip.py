import gzip
import base64


def encode_and_zip(archivo):
    try:
        with open(archivo, 'rb') as f:
            contenido_original = f.read()

        contenido_comprimido = gzip.compress(contenido_original)
        contenido_base64 = base64.b64encode(contenido_comprimido).decode('utf-8')

        return contenido_base64
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None


class EncodeAndZip:
    pass
