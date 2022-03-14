import json
from kodipydent import Kodi # type: ignore


class KodiAPI:
    def __init__(self, port, ip='localhost'):
        self.my_kodi = Kodi(ip, port)

    def obtenerToken(self):
        return self.my_kodi.Application.GetProperties()

#Login with default kodi/kodi credentials
my_kodi = Kodi('localhost', port=10080)

#Login with custom credentials
#kodi = XBMC("http://YOURHOST/jsonrpc", "login", "password")

#print(my_kodi)

def obtenerTodo():
    pelis = my_kodi.VideoLibrary.GetMovies()
    series = my_kodi.VideoLibrary.GetTVShows()
    library = my_kodi.VideoLibrary.Export()
    dicLibrary = {'pelis': pelis['result'], 'series': series['result']}
    library['result'] = dicLibrary
    #library['pelis'] = pelis['result']
    #library['series'] = series['result']
    return library

def obtenerPelisFiltro(filtro):
    pelis=my_kodi.VideoLibrary.GetGenres(type='movie')
    print(pelis)
    #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "title", "value": "A"})

    #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "title", "value": "A"}, sort={"method": "label", "order": "descending"})

    #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "title", "value": "Avatar"}, properties=["title", "thumbnail", "imdbnumber", "year", "plot", "rating", "genre"])

    #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "startswith", "field": "title", "value": "A"}, properties=[ "year", "rating", "genre"])

    #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"or": [{"operator": "startswith", "field": "title", "value": "A"}, {"operator": "startswith", "field": "title", "value": "The A"}]}, properties=["year", "rating", "genre"])

    #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "year", "value": "2009"}, properties=["year", "rating", "genre"])

    peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "genre", "value": filtro}, properties=["year", "rating", "genre"])

    return peliFil

def obtenerPelis():
    return my_kodi.VideoLibrary.GetMovies()

def obtenerPeliDetalles(idPeli):
    return my_kodi.VideoLibrary.GetMovieDetails(movieid=idPeli, properties=["title", "playcount", "runtime", "director", "studio", "year", "plot", "genre", "rating", "mpaa", "imdbnumber", "votes", "lastplayed", "originaltitle", "trailer", "tagline", "plotoutline", "writer", "country", "top250", "sorttitle", "set", "showlink", "thumbnail", "fanart", "tag", "art", "resume", "userrating", "ratings", "dateadded", "premiered", "uniqueid"])
    #return my_kodi.VideoLibrary.GetMovieDetails(movieid=idPeli, properties=["title", "playcount", "runtime"])

def obtenerSeries():
    return my_kodi.VideoLibrary.GetTVShows()

def obtenerSerieDetalles(idSerie):
    return my_kodi.VideoLibrary.GetMovieDetails(tvshowid=idSerie, properties=["title", "playcount", "runtime", "director", "plot", "rating", "votes", "lastplayed", "writer", "firstaired", "productioncode", "season", "episode", "originaltitle", "thumbnail", "fanart", "art", "resume", "userrating", "ratings", "dateadded", "uniqueid"])

def obtenerPortadas():
    portadas = my_kodi.VideoLibrary.GetAvailableArt()
    return portadas

#my_kodi.Player.Open(item={'movieid':1})
#{'id': '5ab9dab104304ed28268fc1c53f846f4', 'jsonrpc': '2.0', 'result': 'OK'}
def reproducirPelisOLD(idPeli, token):
    peli={'movieid':idPeli}
    my_kodi.Player.Open(item=peli)
    {'id': token, 'jsonrpc': '2.0', 'result': 'OK'}

def reproducirPelis(idPeli, token):
    #peli={'movieid':idPeli}
    #my_kodi.Player.Open(item=peli)
    my_kodi.Player.Open(item={'movieid':idPeli})
    #peli={'label': 'Avatar'}
    #my_kodi.Player.Open(item=peli)

def reproducirSeries(idSerie, token):
    peli={'tvshowid':idSerie}
    my_kodi.Player.Open(item=peli)
    {'id': token, 'jsonrpc': '2.0', 'result': 'OK'}

def cambiarVolumen(vol):
    my_kodi.Application.SetVolume(volume=vol)

#my_kodi.Input.ExecuteAction("back")
def ejecutarComando(comando):
    my_kodi.Input.ExecuteAction(action=comando)

#PlayPause(playerid[, username, password, play])
def playPause():
    my_kodi.Player.PlayPause(playerid=1,play='toggle')

#Stop(playerid[, username, password])
def stop():
    my_kodi.Player.Stop(playerid=1)

#my_kodi.GUI.ActivateWindow(window="home")
def activarVentana(ventana):
    my_kodi.GUI.ActivateWindow(window=ventana)





#Open([, username, password, item, options])

library = obtenerTodo()
print(library)

'''
with open('readme.txt', 'w') as f:
    f.write(str(my_kodi))

with open('readme.json', 'w') as f:
    json.dump(my_kodi, f)
'''