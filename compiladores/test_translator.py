import unittest
from translator import process_file

class TestTranslator(unittest.TestCase):
    def test_load_image(self):
        # Prueba la carga de una imagen
        process_file("instrucciones_load_image.txt")
        # Agrega aserciones para verificar que la imagen se haya cargado correctamente

    def test_show_image(self):
        # Prueba mostrar una imagen
        process_file("instrucciones_show_image.txt")
        # Agrega aserciones para verificar que la imagen se haya mostrado correctamente

    def test_save_image(self):
        # Prueba guardar una imagen
        process_file("instrucciones_save_image.txt")
        # Agrega aserciones para verificar que la imagen se haya guardado correctamente

    # Agrega más métodos de prueba para otras características de tu gramática

if __name__ == '__main__':
    unittest.main()
