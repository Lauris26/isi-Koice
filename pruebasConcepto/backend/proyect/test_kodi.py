import unittest
import kodi


class TestKodi(unittest.TestCase):

    def test_kodi_obtenerTodo(self):
        library=kodi.obtenerTodo()
        self.assertNotEqual(library, None, "Should be not None")
    
    def test_kodi_obtenerPelis(self):
        library=kodi.obtenerPelis()
        self.assertNotEqual(library, None, "Should be not None")

    def test_kodi_obtenerSeries(self):
        library=kodi.obtenerPelis()
        self.assertNotEqual(library, None, "Should be not None")


if __name__ == '__main__':
    unittest.main()