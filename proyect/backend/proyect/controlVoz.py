from kodiApi import KodiAPI as kodi


def filtrarSintasisVoz(funcion, dic=""):
    textoVoz=""
    if funcion =='obtenerPelis':
        textoJson=kodi.obtenerPelis()
        textoVoz=filtrarPelis(textoJson)
    elif funcion =='obtenerSeries':
        textoJson=kodi.obtenerSeries()
        textoVoz=filtrarSeries(textoJson)
    elif funcion =='reproPeli':
        peli_id=dic['entities'][0]['value']
        kodi.reproducirPelis(peli_id)
        textoVoz="reproduciendo la pelicula numero "+str(peli_id)
    elif funcion =='reproSerie':
        serie_id=dic['entities'][0]['value']
        kodi.reproducirSeries(serie_id)
        textoVoz="reproduciendo la serie numero "+str(serie_id)
    elif funcion =='playPausa':
        kodi.playPause()
        textoVoz="pausando el video"
    elif funcion =='stop':
        kodi.stop()
        textoVoz="parando el video"
    elif funcion =='cambiarVolumen':
        vol=dic['entities'][0]['value']
        kodi.cambiarVolumen(vol)
        textoVoz="volumen establecido en "+str(vol)

    return textoVoz

def filtrarPelis(textoJson):
    tex= "La lista de peliculas es: "

    for video in textoJson['result']['movies']:
        print(video)
        tex+="película numero "+str(video['movieid'])+" es "+video['label']+" "
    return tex

def filtrarSeries(textoJson):
    tex= "La lista de series es: "

    for video in textoJson['result']['tvshows']:
        print(video)
        tex+="serie numero "+str(video['tvshowid'])+" es "+video['label']+" "
    return tex