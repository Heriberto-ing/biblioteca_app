class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.isbn = isbn.strip()
        self.prestado = False

    def esta_disponible(self):
        return not self.prestado

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.titulo} - {self.autor} | ISBN: {self.isbn} | {estado}"