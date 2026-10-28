from modelos import Libro


class Biblioteca:
    def __init__(self):
        self.libros = []

    def registrar_libro(self, titulo, autor, isbn):
        if not titulo.strip() or not autor.strip() or not isbn.strip():
            raise ValueError("Todos los campos son obligatorios")

        for libro in self.libros:
            if libro.isbn == isbn.strip():
                raise ValueError("El ISBN ya está registrado")

        nuevo_libro = Libro(titulo, autor, isbn)
        self.libros.append(nuevo_libro)
        return nuevo_libro

    def buscar_libro(self, criterio):
        criterio = criterio.strip().lower()
        resultados = []

        for libro in self.libros:
            if criterio in libro.titulo.lower() or criterio in libro.autor.lower() or criterio == libro.isbn.lower():
                resultados.append(libro)

        return resultados

    def prestar_libro(self, isbn, usuario):
        if not usuario.strip():
            raise ValueError("El nombre del usuario es obligatorio")

        for libro in self.libros:
            if libro.isbn == isbn.strip():
                if libro.prestado:
                    raise ValueError("El libro ya está prestado")
                libro.prestado = True
                return f"Préstamo registrado para {usuario}"

        raise ValueError("No se encontró el libro")

    def devolver_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn.strip():
                if not libro.prestado:
                    raise ValueError("El libro ya está disponible")
                libro.prestado = False
                return "Devolución registrada"

        raise ValueError("No se encontró el libro")

    def listar_libros(self):
        return [str(libro) for libro in self.libros]

    def contar_disponibles(self):
        disponibles = 0
        for libro in self.libros:
            if libro.esta_disponible():
                disponibles += 1
        return disponibles

    def cargar_datos_demo(self):
        try:
            self.registrar_libro("Cien años de soledad", "Gabriel García Márquez", "ISBN001")
            self.registrar_libro("El principito", "Antoine de Saint-Exupéry", "ISBN002")
            self.registrar_libro("Don Quijote", "Miguel de Cervantes", "ISBN003")
        except Exception as error:
            print("No se pudieron cargar los datos de ejemplo")
