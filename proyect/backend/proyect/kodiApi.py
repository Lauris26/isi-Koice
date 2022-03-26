import json
from kodipydent import Kodi # type: ignore
from imdbApi import obtenerPortada, obtenerActoresPeli, obtenerPortadaTemporada


class KodiAPI:
    def __init__(self, port1, ip='localhost'):
        #Login with custom credentials
        #self.my_kodi = Kodi("http://YOURHOST/jsonrpc", "login", "password")

        #Login with default kodi/kodi credentials
        self.my_kodi=Kodi(ip, port=port1)
        #self.my_kodi=None
        #print(type(self.my_kodi))

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

    def addPortadaTemporada(self, dicTemporada):
        lisTemporada=[]
        for i, temp in enumerate(dicTemporada['result']['tvshowdetails']):
            dicTemporada={
                'id': i,
                'poster': obtenerPortadaTemporada(temp['label']),
                'titulo': temp['label']
            }
            lisTemporada.append(dicTemporada)
        dicTemporada['result']['seasons']=lisTemporada

        return dicTemporada

    def addActores(self, dicciPelis):
        #print(dicciPelis)
        dicciPelis['result']['moviedetails']['poster']=obtenerPortada(dicciPelis['result']['moviedetails']['title'])
        dicciPelis['result']['moviedetails']['actores']=obtenerActoresPeli(dicciPelis['result']['moviedetails']['title'])
        dicciPelis['result']['moviedetails']['runtime']=int(dicciPelis['result']['moviedetails']['runtime']/60)
        '''
        lisPelis=[]
        for peli in dicciPelis['result']['moviedetails']:
            dicPelis={
                'id': peli['movieid'],
                'poster': obtenerPortada(peli['label']),
                'titulo': peli['label'],
                'resumen': peli['plot'],
                'tiempo' : peli['runtime'],
                'generos': peli['genre'],
                'actores': obtenerActores(peli['label'])
            }
            lisPelis.append(dicPelis)
        dicciPelis['result']['moviedetails']=lisPelis
        '''
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
        #return self.my_kodi.VideoLibrary.GetMovieDetails(movieid=idPeli, properties=["title", "playcount", "runtime", "director", "studio", "year", "plot", "genre", "rating", "mpaa", "imdbnumber", "votes", "lastplayed", "originaltitle", "trailer", "tagline", "plotoutline", "writer", "country", "top250", "sorttitle", "set", "showlink", "thumbnail", "fanart", "tag", "art", "resume", "userrating", "ratings", "dateadded", "premiered", "uniqueid"])
        #return self.my_kodi.VideoLibrary.GetMovieDetails(movieid=idPeli, properties=["title", "runtime", "year", "plot", "genre"])
        return self.addActores(self.my_kodi.VideoLibrary.GetMovieDetails(movieid=idPeli, properties=["title", "runtime", "year", "plot", "genre"]))

    def obtenerPelisFiltro(self, filtro):
        pelis=self.my_kodi.VideoLibrary.GetGenres(type='movie')
        print(pelis)
        #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "title", "value": "A"})

        #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "title", "value": "A"}, sort={"method": "label", "order": "descending"})

        #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "title", "value": "Avatar"}, properties=["title", "thumbnail", "imdbnumber", "year", "plot", "rating", "genre"])

        #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "startswith", "field": "title", "value": "A"}, properties=[ "year", "rating", "genre"])

        #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"or": [{"operator": "startswith", "field": "title", "value": "A"}, {"operator": "startswith", "field": "title", "value": "The A"}]}, properties=["year", "rating", "genre"])

        #peliFil=my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "year", "value": "2009"}, properties=["year", "rating", "genre"])

        peliFil=self.my_kodi.VideoLibrary.GetMovies(filter={"operator": "contains", "field": "genre", "value": filtro}, properties=["year", "rating", "genre"])

        return peliFil


    def obtenerSeries(self):
        #return self.my_kodi.VideoLibrary.GetTVShows()
        return self.addPortadaSerie(self.my_kodi.VideoLibrary.GetTVShows())

    def obtenerSerieTemporadas(self, idSerie):
        #serie={'tvshowid':idSerie}
        #serie={'tvshowid':idSerie, 'season':1}
        #return self.my_kodi.VideoLibrary.GetEpisodes(item=serie)
        return self.my_kodi.VideoLibrary.GetSeasons(tvshowid=idSerie)
        #return self.my_kodi.VideoLibrary.GetEpisodes(tvshowid=3, properties=["title", "rating"])

    def obtenerSerieDetalles(self, idSerie):
        return self.addActoresSerie(self.my_kodi.VideoLibrary.GetTVShowDetails(tvshowid=idSerie, properties=["title", "year", "plot", "season", "episode", "genre"]))

    def obtenerSeriesFiltro(self, filtro):
        print(filtro)
        return self.my_kodi.VideoLibrary.GetTVShows(filter={"operator": "contains", "field": "genre", "value": filtro}, properties=["title", "thumbnail", "imdbnumber", "year", "plot", "rating", "genre"])

    #my_kodi.Player.Open(item={'movieid':1})
    #{'id': '5ab9dab104304ed28268fc1c53f846f4', 'jsonrpc': '2.0', 'result': 'OK'}
    def reproducirPelisOLD(self, idPeli, token):
        peli={'movieid':idPeli}
        self.my_kodi.Player.Open(item=peli)
        {'id': token, 'jsonrpc': '2.0', 'result': 'OK'}

    def reproducirPelis(self, idPeli, token):
        #peli={'movieid':idPeli}
        #my_kodi.Player.Open(item=peli)
        self.my_kodi.Player.Open(item={'movieid':idPeli})
        #peli={'label': 'Avatar'}
        #my_kodi.Player.Open(item=peli)

    def reproducirSeries(self, idSerie, token):
        serie={'tvshowid':idSerie, "seasonid":3}
        self.my_kodi.Player.Open(item=serie)
        {'id': token, 'jsonrpc': '2.0', 'result': 'OK'}

    def cambiarVolumen(self, vol):
        self.my_kodi.Application.SetVolume(volume=vol)

    #my_kodi.Input.ExecuteAction("back")
    def ejecutarComando(self, comando):
        self.my_kodi.Input.ExecuteAction(action=comando)

    #PlayPause(playerid[, username, password, play])
    def playPause(self):
        self.my_kodi.Player.PlayPause(playerid=1,play='toggle')

    #Stop(playerid[, username, password])
    def stop(self):
        self.my_kodi.Player.Stop(playerid=1)


