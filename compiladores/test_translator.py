import unittest
import translator
from translator import process_file

class TestTranslator(unittest.TestCase):
    def test_load_image(self):
        # Prueba la carga de una imagen
        process_file("instrucciones_load_image.txt")

    def test_show_image(self):
        # Prueba mostrar una imagen
        process_file("instrucciones_show_image.txt")
    
    def test_gen_matrix(self):
        # Prueba para generar una matriz
        process_file("instrucciones_lista.txt")


if __name__ == '__main__':
    unittest.main()
