import unittest
from biblioteca import Biblioteca


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.biblioteca.registrar_libro(
            "Cien años de soledad",
            "Gabriel García Márquez",
            "ISBN001"
        )

    def test_registrar_libro(self):
        self.assertEqual(len(self.biblioteca.libros), 1)

    def test_rechazar_isbn_duplicado(self):
        with self.assertRaises(ValueError):
            self.biblioteca.registrar_libro(
                "Otro libro", "Otro autor", "ISBN001"
            )

    def test_prestar_y_devolver_libro(self):
        self.biblioteca.prestar_libro("ISBN001", "Ana")
        self.assertEqual(self.biblioteca.contar_disponibles(), 0)

        self.biblioteca.devolver_libro("ISBN001")
        self.assertEqual(self.biblioteca.contar_disponibles(), 1)

    def test_buscar_por_titulo(self):
        resultados = self.biblioteca.buscar_libro("soledad")
        self.assertEqual(len(resultados), 1)

    def test_rechazar_prestamo_de_libro_prestado(self):
        self.biblioteca.prestar_libro("ISBN001", "Ana")
        with self.assertRaises(ValueError):
            self.biblioteca.prestar_libro("ISBN001", "Luis")


if __name__ == "__main__":
    unittest.main()
