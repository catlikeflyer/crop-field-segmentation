import unittest
import translator
from translator import process_file

class TestTranslator(unittest.TestCase):
    def test_load_image(self):
        # Prueba la carga de una imagen
        process_file("pruebas_load_image.txt")

    def test_show_image(self):
        # Prueba mostrar una imagen
        process_file("pruebas_show_image.txt")
    
    def test_gen_matrix(self):
        # Prueba para generar una matriz
        process_file("instrucciones_lista.txt")

    def test_algorithms(self):
        #Prueba para generar un histograma
        process_file("pruebas_algoritmos.txt")

    def test_histograms(self):
        #Prueba para generar un histograma
        process_file("pruebas_histograma.txt")

if __name__ == '__main__':
    unittest.main()
