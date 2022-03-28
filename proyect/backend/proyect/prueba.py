from kodiApi import KodiAPI

IP_KODI="127.0.0.1"
PORT_KODI=10080

def obtenerKodi(IP_KODI, PORT_KODI):
    try:
        kodi=KodiAPI(PORT_KODI, IP_KODI)
        print("Servidor kodi abierto correctamente")

    except Exception as e:
        print("No se ha podido abrir el servidor kodi")
        print("excepcion: ", e)
        exit(0)
    return kodi

kodi = obtenerKodi(IP_KODI, PORT_KODI)

print(kodi.obtenerSeries())

print(kodi.obtenerSerieTemporadas(1))

print(kodi.obtenerSerieEpisodios(1))

kodi.reproducirSeries(1)