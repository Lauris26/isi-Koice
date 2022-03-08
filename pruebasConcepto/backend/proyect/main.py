from flask import Flask, jsonify
import kodi
from kodi import obtenerPelis
from kodi import reproducirPelis

app = Flask(__name__)

@app.route("/")
def home():
    return kodi.obtenerTodo()

@app.route("/kodi/pelis", methods=['GET', 'POST'])
def kodi_pelis():
    pelis=obtenerPelis()
    return jsonify(pelis)

@app.route("/kodi/series", methods=['GET', 'POST'])
def kodi_series():
    series=kodi.obtenerSeries()
    return jsonify(series)

@app.route("/kodi/pelis/<int:peli_id>", methods=['GET', 'POST'])
def kodi_pelis_id(peli_id):
    pelis=obtenerPelis()
    token=pelis['id']
    print(token)
    movies=pelis['result']['movies'][peli_id-1]
    print(movies)
    #peli=pelis[peli_id]
    reproducirPelis(peli_id, token)
    return jsonify({'id': token, 'jsonrpc': '2.0', 'result': 'OK', 'peli_id': movies})

if __name__ == '__main__':
    app.run()