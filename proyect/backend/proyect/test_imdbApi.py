import unittest
import imdbApi

class TestImdbApi(unittest.TestCase):

    def test_kodi_obtenerPortada(self):
        dato=imdbApi.obtenerPortada('avatar')
        print(dato)
        self.assertNotEqual(dato, None, "Should be not None")

    def test_kodi_obtenerActoresPeli(self):
        dato=imdbApi.obtenerActoresPeli('avatar')
        print(dato)
        self.assertNotEqual(dato, None, "Should be not None")

    def test_kodi_obtenerPortadaTemporada(self):
        dato=imdbApi.obtenerPortadaTemporada('Black Mirror')
        print(dato)
        self.assertNotEqual(dato, None, "Should be not None")

