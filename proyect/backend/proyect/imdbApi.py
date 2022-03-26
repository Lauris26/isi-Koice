from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

def obtenerPortada(titulo):
    video = ia.search_movie(titulo)
    #mocieID = movies[0].movieID
    #print(mocieID)
    #movie=ia.get_movie(mocieID)
    #print(movie.get('cover url'))
    #print(movie.get('full-size cover url'))
    #return movie.get('full-size cover url')
    #print(movies)
    if video[0]['title'].lower()==titulo.lower():
        #print(movies[0]['cover url'])
        #return movies[0]['cover url']
        return video[0]['full-size cover url']

def obtenerActoresPeli(titulo):
    movies = ia.search_movie(titulo)
    mocieID = movies[0].movieID
    #print(mocieID)
    movie=ia.get_movie(mocieID)
    cast=movie.get('cast')
    #print(cast)
    listActor=[]
    for i in range(5):
        personaID=cast[i].personID
        persona=ia.get_person(personaID)
        foto=persona.get('full-size headshot')
        dicActor={'id': i,
                'foto': foto,
                'nombre': persona.get('name')
                }
        listActor.append(dicActor)
    #print(movie.get('full-size cover url'))
    #return movie.get('full-size cover url')
    #print(movies)
    if movie['title'].lower()==titulo.lower():
        #print(movies[0]['cover url'])
        #return movies[0]['cover url']
        return listActor

def obtenerPortadaSerie(titulo):
    series=ia.search_movie(titulo)
    if series[0]['title'].lower()==titulo.lower():
        return series[0]['full-size cover url']



if __name__ == '__main__':
    obtenerPortadaSerie("Black Mirror")