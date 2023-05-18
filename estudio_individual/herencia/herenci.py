class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def hacer_sonido(self):
        print("El perro ladra.")

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color
    
    def hacer_sonido(self):
        print("El gato maulla.")

# Crear instancias de las clases derivadas
mi_perro = Perro("Max", "Labrador")
mi_gato = Gato("Luna", "Negro")

# Acceder a los atributos y métodos heredados
print(mi_perro.nombre)  # Salida: Max
print(mi_perro.raza)  # Salida: Labrador
mi_perro.hacer_sonido()  # Salida: El perro ladra.

print(mi_gato.nombre)  # Salida: Luna
print(mi_gato.color)  # Salida: Negro
mi_gato.hacer_sonido()  # Salida: El gato maulla.
