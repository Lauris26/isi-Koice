import unittest
import kodiApi as kodi

IP_KODI="127.0.0.1"
PORT_KODI=10080

class TestKodi(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestKodi, self).__init__(*args, **kwargs)
        self.my_kodi=None

    def setUp(self):
        super(TestKodi, self).setUp()
        self.my_kodi=kodi.KodiAPI(PORT_KODI, IP_KODI)
    '''
    def test_kodi_obtenerTodo(self):
        library=self.my_kodi.obtenerTodo()
        print(library)
        self.assertNotEqual(library, None, "Should be not None")
    
    def test_kodi_obtenerPelis(self):
        library=self.my_kodi.obtenerPelis()
        print(library)
        self.assertNotEqual(library, None, "Should be not None")

    def test_kodi_obtenerSeries(self):
        library=self.my_kodi.obtenerSeries()
        print(library)
        self.assertNotEqual(library, None, "Should be not None")
    '''
    
    def test_kodi_obtenerSerieTemporadas(self):
        library=self.my_kodi.obtenerSerieTemporadas(1)
        print(library)
        primer_elemento = list(library)[0]
        print(primer_elemento)
        self.assertNotEqual(primer_elemento, 'error', "Should be not None")

    def test_kodi_obtenerSerieDetalles(self):
        library=self.my_kodi.obtenerSerieDetalles(1)
        print(library)
        self.assertNotEqual(library, None, "Should be not None")
    '''
    
    def test_kodi_obtenerSerieDetalles(self):
        library=self.my_kodi.obtenerSerieDetalles(1)
        print(library)
        self.assertNotEqual(library, None, "Should be not None")

    def test_kodi_obtenerSeriesFiltro(self):
        library=self.my_kodi.obtenerSeriesFiltro('Drama')
        print(library)
        self.assertNotEqual(library, None, "Should be not None")
    '''


if __name__ == '__main__':
    unittest.main()