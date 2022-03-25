from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

def obtenerPortada(titulo):
    movies = ia.search_movie(titulo)
    #print(movies)
    if movies[0]['title'].lower()==titulo.lower():
        #print(movies[0]['cover url'])
        return movies[0]['cover url']



obtenerPortada("avatar")