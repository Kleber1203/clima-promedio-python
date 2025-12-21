# Ejemplo del mundo real: Sistema de Biblioteca

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' fue prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' fue devuelto.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"{self.titulo} - {self.autor} | Estado: {estado}")


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            libro.mostrar_info()


# Prueba del sistema
libro1 = Libro("Cálculo", "Stewart")
libro2 = Libro("Python Básico", "Autor X")

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros()
libro1.prestar()
biblioteca.mostrar_libros()
