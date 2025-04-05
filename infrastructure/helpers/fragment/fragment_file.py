def fragment_and_send(contenido, ws, id_audio, tamanio_fragmento=1024):
    global indice_fragmento
    fragmentos = [contenido[i:i + tamanio_fragmento] for i in range(0, len(contenido), tamanio_fragmento)]

    total_fragmentos = len(fragmentos)

    for i, fragmento in enumerate(fragmentos):
        try:
            indice_fragmento = i + 1
            mensaje = f"upload:{id_audio}:{indice_fragmento}:{total_fragmentos}:{fragmento}"
            print(f"Enviando fragmento {indice_fragmento}/{total_fragmentos}")
            ws.send(mensaje)
            ws.recv()
            print(f"Fragmento {indice_fragmento} enviado con éxito.")
        except Exception as e:
            print(f"Error al enviar el fragmento {indice_fragmento}: {e}")
            break

    print("Todos los fragmentos fueron enviados con éxito.")


class FragmentFile:
    pass
