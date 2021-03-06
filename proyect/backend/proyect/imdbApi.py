from imdb import Cinemagoer

ia = Cinemagoer()

def obtenerPortada(titulo):
    video = ia.search_movie(titulo)
    if video[0]['title'].lower()==titulo.lower():
        return video[0]['full-size cover url']

def obtenerActoresPeli(titulo):
    movies = ia.search_movie(titulo)
    mocieID = movies[0].movieID
    movie=ia.get_movie(mocieID)
    cast=movie.get('cast')
    listActor=[]
    for i in range(5):
        personaID=cast[i].personID
        persona=ia.get_person(personaID)
        foto=persona.get('full-size headshot')
        if foto==None:
            foto='https://postimg.cc/LgFbhDWC'
        dicActor={'id': i,
                'foto': foto,
                'nombre': persona.get('name')
                }
        listActor.append(dicActor)
    if movie['title'].lower()==titulo.lower():
        return listActor
    

def obtenerPortadaTemporada(titulo, temporada=1):
    series=ia.search_movie(titulo)
    serieID=series[0].movieID
    serie=ia.get_movie(serieID)
    tempo=serie['seasons']
    if series[0]['title'].lower()==titulo.lower():
        return series[0]['full-size cover url']



if __name__ == '__main__':
    obtenerActoresPeli("Black Mirror")