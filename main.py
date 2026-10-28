from biblioteca import Biblioteca

def mostrar_menu():
    print("\n SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Listar libros")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Ver libros disponibles")
    print("0. Salir")


def ejecutar():
    biblioteca = Biblioteca()
    biblioteca.cargar_datos_demo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                isbn = input("ISBN: ")
                libro = biblioteca.registrar_libro(titulo, autor, isbn)
                print("Libro registrado:", libro)

            elif opcion == "2":
                criterio = input("Título, autor o ISBN: ")
                resultados = biblioteca.buscar_libro(criterio)
                if resultados:
                    for libro in resultados:
                        print(libro)
                else:
                    print("No se encontraron libros")

            elif opcion == "3":
                for libro in biblioteca.listar_libros():
                    print(libro)

            elif opcion == "4":
                isbn = input("ISBN del libro: ")
                usuario = input("Nombre del usuario: ")
                print(biblioteca.prestar_libro(isbn, usuario))

            elif opcion == "5":
                isbn = input("ISBN del libro: ")
                print(biblioteca.devolver_libro(isbn))

            elif opcion == "6":
                print("Libros disponibles:", biblioteca.contar_disponibles())

            elif opcion == "0":
                print("Programa finalizado")
                break

            else:
                print("Opción inválida")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    ejecutar()
