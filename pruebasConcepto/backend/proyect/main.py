from flask import Flask, jsonify, request
import kodi
import json

app = Flask(__name__)

@app.route("/")
def home():
    return kodi.obtenerTodo()

@app.route("/kodi/pelis", methods=['GET', 'POST'])
def kodi_pelis():
    pelis=kodi.obtenerPelis()
    return jsonify(pelis)

@app.route("/kodi/series", methods=['GET', 'POST'])
def kodi_series():
    series=kodi.obtenerSeries()
    return jsonify(series)

@app.route("/kodi/pelis/<int:peli_id>", methods=['GET', 'POST'])
def kodi_pelis_id(peli_id):
    pelis=kodi.obtenerPelis()
    token=pelis['id']
    print(token)
    movies=pelis['result']['movies'][peli_id-1]
    print(movies)
    #peli=pelis[peli_id]
    kodi.reproducirPelis(peli_id, token)
    return jsonify({'id': token, 'jsonrpc': '2.0', 'result': 'OK', 'peli_id': movies})

@app.route("/kodi/pelis/<int:serie_id>", methods=['GET', 'POST'])
def kodi_series_id(serie_id):
    series=kodi.obtenerSeries()
    token=series['id']
    print(token)
    movies=series['result']['tvshows'][serie_id-1]
    print(movies)
    #peli=pelis[peli_id]
    kodi.reproducirSeries(serie_id, token)
    return jsonify({'id': token, 'jsonrpc': '2.0', 'result': 'OK', 'serie_id': movies})

@app.route("/kodi/play_pause", methods=['GET', 'POST'])
def kodi_play_pausa():
    series=kodi.obtenerSeries()
    token=series['id']
    kodi.playPause()
    return jsonify({'id': token, 'jsonrpc': '2.0', 'result': 'OK'})

@app.route("/kodi/stop", methods=['GET', 'POST'])
def kodi_stop():
    series=kodi.obtenerSeries()
    token=series['id']
    kodi.stop()
    return jsonify({'id': token, 'jsonrpc': '2.0', 'result': 'OK'})



@app.route("/test/v2", methods=['POST'])
def testinput():
    textoDic=json.loads(request.data.decode('utf-8'))
    print("RECIVIDO DE VOZ")
    print(textoDic)
    funcion=textoDic['intent']['name']
    print("funcion : ",funcion)
    print(textoDic['entities'])
    #print(textoDic['entities'][0]['value'])
    #texto=switchFuncVoz(funcion)
    #print(texto['result']['movies'])
    tex = filtrarSintasisVoz(funcion, textoDic)

    #tex= "has ejecutado la funcion "+funcion+" ,"
    print(tex)
    return jsonify({
    "speech": {
        "text": tex
        }
    })

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
        kodi_pelis_id(peli_id)
        textoVoz="reproduciendo la pelicula numero "+str(peli_id)
    elif funcion =='reproSerie':
        pass
    elif funcion =='playPausa':
        kodi_play_pausa()
        textoVoz="pausando el video"
    elif funcion =='stop':
        kodi_stop()
        textoVoz="parando el video"

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

if __name__ == '__main__':
    app.run()