class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)

    def mostrar_libros(self):
        if self.libros_disponibles:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros_disponibles:
                print("Título: , Autor: , Año de publicación: ")
        else:
            print("No hay libros disponibles en la biblioteca.")