import json
from kodipydent import Kodi # type: ignore

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

def obtenerPelis():
    return my_kodi.VideoLibrary.GetMovies()

def obtenerSeries():
    return my_kodi.VideoLibrary.GetTVShows()

def obtenerPortadas():
    portadas = my_kodi.VideoLibrary.GetAvailableArt()
    return portadas

#my_kodi.Player.Open(item={'movieid':1})
#{'id': '5ab9dab104304ed28268fc1c53f846f4', 'jsonrpc': '2.0', 'result': 'OK'}
def reproducirPelis(idPeli, token):
    peli={'movieid':idPeli}
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