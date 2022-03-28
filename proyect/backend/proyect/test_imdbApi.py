import unittest
import imdbApi

class TestImdbApi(unittest.TestCase):

    def test_kodi_obtenerPortada(self):
        dato=imdbApi.obtenerPortada('avatar')
        print(dato)
        self.assertNotEqual(dato, None, "Should be not None")