# proyect/__init__.py
# proyect/kodiApi.py
from flask_cors import CORS
from flask import Flask, jsonify, request
from kodiApi import KodiAPI
import json
import controlVoz

app = Flask(__name__)
CORS(app)

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

@app.route("/")
def home():
    return kodi.obtenerTodo()

@app.route("/kodi/pelis", methods=['GET', 'POST'])
def kodi_pelis():
    pelis=kodi.obtenerPelis()
    return jsonify(pelis)

@app.route("/kodi/pelidetalles/<int:peli_id>", methods=['GET', 'POST'])
def kodi_pelis_detalles(peli_id):
    pelis=kodi.obtenerPeliDetalles(peli_id)
    return jsonify(pelis)

@app.route("/kodi/pelis/<string:filtro>", methods=['GET', 'POST'])
def kodi_pelis_filtro(filtro):
    print("dentro de filtro: ", filtro)
    try:
        tipo=filtro.split("_")[0]
        dato=filtro.split("_")[1]
        print("tipo: ", tipo)
        print("dato: ", dato)
        pelis=kodi.obtenerPelisFiltro(dato)
        return jsonify(pelis)
    except:
        print("error en filtro")
    finally:
        pelis=kodi.obtenerPelisFiltro(filtro)
        return jsonify(pelis)

@app.route("/kodi/play/peli/<int:peli_id>", methods=['GET', 'POST'])
def kodi_play_pelis_id(peli_id):
    kodi.reproducirPelis(peli_id)

############# SERIES #############    


@app.route("/kodi/series", methods=['GET', 'POST'])
def kodi_series():
    series=kodi.obtenerSeries()
    return jsonify(series)

@app.route("/kodi/series/<int:serie_id>", methods=['GET', 'POST'])
def kodi_series_temporadas(serie_id):
    print(serie_id)
    series=kodi.obtenerSerieTemporadas(serie_id)
    return jsonify(series)

@app.route("/kodi/play/serie/<int:serie_id>", methods=['GET', 'POST'])
def kodi_play_series_id(serie_id):
    kodi.reproducirSeries(serie_id)

@app.route("/kodi/seriedetalles/<int:serie_id>", methods=['GET', 'POST'])
def kodi_serie_detalles(serie_id):
    serie=kodi.obtenerSerieDetalles(serie_id)
    return jsonify(serie)

############ CONTROLES ###############

@app.route("/kodi/play_pause", methods=['GET', 'POST'])
def kodi_play_pausa():
    kodi.playPause()

@app.route("/kodi/stop", methods=['GET', 'POST'])
def kodi_stop():
    kodi.stop()

@app.route("/kodi/next", methods=['GET', 'POST'])
def kodi_next():
    kodi.avanceRapido(2)

@app.route("/kodi/back", methods=['GET', 'POST'])
def kodi_back():
    kodi.retrocesoRapido(-2)

@app.route("/kodi/cambiarVolumen/<int:vol>", methods=['GET', 'POST'])
def kodi_cambiarVolumen(vol):
    kodi.cambiarVolumen(vol)

############## CONTROL VOZ ##############


@app.route("/test/v2", methods=['POST'])
def testinput():
    try:
        textoDic=json.loads(request.data.decode('utf-8'))
        print("RECIVIDO DE VOZ")
        print(textoDic)
        funcion=textoDic['intent']['name']
        print("funcion : ",funcion)
        print(textoDic['entities'])
        #print(textoDic['entities'][0]['value'])
        #texto=switchFuncVoz(funcion)
        #print(texto['result']['movies'])
        tex = controlVoz.filtrarSintasisVoz(kodi, funcion, textoDic)
    except Exception as e:
        print("No se ha podido entender el comando de voz")
        print("excepcion: ", e)

    #tex= "has ejecutado la funcion "+funcion+" ,"
    print(tex)
    return jsonify({
    "speech": {
        "text": tex
        }
    })


'''
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
        kodi_play_pelis_id(peli_id)
        textoVoz="reproduciendo la pelicula numero "+str(peli_id)
    elif funcion =='reproSerie':
        serie_id=dic['entities'][0]['value']
        kodi_play_series_id(serie_id)
        textoVoz="reproduciendo la serie numero "+str(serie_id)
    elif funcion =='playPausa':
        kodi_play_pausa()
        textoVoz="pausando el video"
    elif funcion =='stop':
        kodi_stop()
        textoVoz="parando el video"
    elif funcion =='cambiarVolumen':
        vol=dic['entities'][0]['value']
        kodi_cambiarVolumen(vol)
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


@app.route("/test/v1", methods=['POST'])
def testinput2():
    print("\n\targumentos:")
    print(request.args)
    print("\n\tformulario:")
    print(request.form)
    print("\n\tobjeto adjunto:")
    print(request.data)
    print("\n\tcabecera:")
    print(request.headers)
    textoDic=json.loads(request.data.decode('utf-8'))
    texto=textoDic['intent']['name']
    print("texto tal: ",texto)
    tex= "has ejecutado la funcion "+texto
    return jsonify({
    "speech": {
        "text": tex
        }
    })

def switchFuncVoz(funcion):
    switch = {
        'obtenerPelis' : kodi.obtenerPelis(),
        'obtenerSeries' : kodi.obtenerSeries(),
    }
    return switch.get(funcion, "invalido")

'''


if __name__ == '__main__':
    app.run()