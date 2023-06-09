class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo


class CuentaPersonal(Usuario):
    def __init__(self, nombre, apellido, correo, direccion, telefono):
        super().__init__(nombre, apellido, correo)
        self.direccion = direccion
        self.telefono = telefono


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, correo, numero_estudiante):
        super().__init__(nombre, apellido, correo)
        self.numero_estudiante = numero_estudiante


class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion


class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)

    def mostrar_libros(self):
        if self.libros_disponibles:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros_disponibles:
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, Año de publicación: {libro.anio_publicacion}")
        else:
            print("No hay libros disponibles en la biblioteca.")


# Ejemplo de uso del programa
biblioteca = Biblioteca()

# Agregar libros a la biblioteca
libro1 = Libro("Python Crash Course", "Eric Matthes", 2019)
libro2 = Libro("Clean Code", "Robert C. Martin", 2008)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Mostrar libros disponibles
biblioteca.mostrar_libros()

# Crear una cuenta personal
cuenta_personal = CuentaPersonal("John", "Doe", "johndoe@example.com", "123 Main St", "555-1234")

# Crear un estudiante
estudiante = Estudiante("Jane", "Smith", "janesmith@example.com", "123456789")

# Imprimir información de la cuenta personal y el estudiante
print(f"Cuenta personal: {cuenta_personal.nombre} {cuenta_personal.apellido}, Correo: {cuenta_personal.correo}, "
      f"Dirección: {cuenta_personal.direccion}, Teléfono: {cuenta_personal.telefono}")

print(f"Estudiante: {estudiante.nombre} {estudiante.apellido}, Correo: {estudiante.correo}, "
      f"Número de estudiante: {estudiante.numero_estudiante}")
