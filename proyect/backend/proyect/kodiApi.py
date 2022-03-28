from kodipydent import Kodi # type: ignore
from imdbApi import obtenerPortada, obtenerActoresPeli, obtenerPortadaTemporada


class KodiAPI:
    def __init__(self, port1, ip='localhost'):
        #Login with custom credentials
        #self.my_kodi = Kodi("http://YOURHOST/jsonrpc", "login", "password")

        #Login with default kodi/kodi credentials
        self.my_kodi=Kodi(ip, port=port1)

    def addPortada(self, dicciPelis):
        lisPelis=[]
        for peli in dicciPelis['result']['movies']:
            dicPelis={
                'id': peli['movieid'],
                'poster': obtenerPortada(peli['label']),
                'titulo': peli['label']
            }
            lisPelis.append(dicPelis)
        dicciPelis['result']['movies']=lisPelis

        return dicciPelis

    def addPortadaSerie(self, dicVideo):
        lisVideo=[]
        for serie in dicVideo['result']['tvshows']:
            dicPelis={
                'id': serie['tvshowid'],
                'poster': obtenerPortada(serie['label']),
                'titulo': serie['label']
            }
            lisVideo.append(dicPelis)
        dicVideo['result']['tvshows']=lisVideo

        return dicVideo

    def addActores(self, dicciPelis):
        dicciPelis['result']['moviedetails']['poster']=obtenerPortada(dicciPelis['result']['moviedetails']['title'])
        dicciPelis['result']['moviedetails']['actores']=obtenerActoresPeli(dicciPelis['result']['moviedetails']['title'])
        dicciPelis['result']['moviedetails']['runtime']=int(dicciPelis['result']['moviedetails']['runtime']/60)
        return dicciPelis

    def addActoresSerie(self, dicciSeries):
        dicciSeries['result']['tvshowdetails']['poster']=obtenerPortada(dicciSeries['result']['tvshowdetails']['title'])
        dicciSeries['result']['tvshowdetails']['actores']=obtenerActoresPeli(dicciSeries['result']['tvshowdetails']['title'])
        dicciSeries['result']['tvshowdetails']['seasons']=self.obtenerSerieTemporadas(dicciSeries['result']['tvshowdetails']['tvshowid'])['result']['seasons']
        return dicciSeries
        
    def obtenerToken(self):
        return self.my_kodi.Application.GetProperties()

    def obtenerTodo(self):
        pelis = self.my_kodi.VideoLibrary.GetMovies()
        series = self.my_kodi.VideoLibrary.GetTVShows()
        library = self.my_kodi.VideoLibrary.Export()
        dicLibrary = {'pelis': pelis['result'], 'series': series['result']}
        library['result'] = dicLibrary
        #library['pelis'] = pelis['result']
        #library['series'] = series['result']
        return library
    

    def obtenerPelis(self):
        return self.addPortada(self.my_kodi.VideoLibrary.GetMovies())

    def obtenerPeliDetalles(self, idPeli):
        return self.addActores(self.my_kodi.VideoLibrary.GetMovieDetails(movieid=idPeli, properties=["title", "runtime", "year", "plot", "genre"]))

    def obtenerPelisFiltro(self, filtro):
        #pelis=self.my_kodi.VideoLibrary.GetGenres(type='movie')
        peliFil=self.my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "genre", "value": filtro}, properties=["title", "runtime", "year", "plot", "genre"])

        return peliFil

    def obtenerSeries(self):
        return self.addPortadaSerie(self.my_kodi.VideoLibrary.GetTVShows())

    def obtenerSerieTemporadas(self, idSerie):
        return self.my_kodi.VideoLibrary.GetSeasons(tvshowid=idSerie)

    def obtenerSerieDetalles(self, idSerie):
        return self.addActoresSerie(self.my_kodi.VideoLibrary.GetTVShowDetails(tvshowid=idSerie, properties=["title", "year", "plot", "season", "episode", "genre"]))

    def obtenerSeriesFiltro(self, filtro):
        print(filtro)
        return self.my_kodi.VideoLibrary.GetTVShows(filter={"operator": "contains", "field": "genre", "value": filtro}, properties=["title", "thumbnail", "imdbnumber", "year", "plot", "rating", "genre"])

    def reproducirPelis(self, idPeli):
        self.my_kodi.Player.Open(item={'movieid':idPeli})

    def reproducirSeries(self, idSerie, token):
        serie={'tvshowid':idSerie, "seasonid":3}
        self.my_kodi.Player.Open(item=serie)
        {'id': token, 'jsonrpc': '2.0', 'result': 'OK'}

    def cambiarVolumen(self, vol):
        self.my_kodi.Application.SetVolume(volume=vol)

    def playPause(self):
        self.my_kodi.Player.PlayPause(playerid=1,play='toggle')

    def stop(self):
        self.my_kodi.Player.Stop(playerid=1)

    #my_kodi.Input.ExecuteAction("back")
    def ejecutarComando(self, comando):
        self.my_kodi.Input.ExecuteAction(action=comando)


