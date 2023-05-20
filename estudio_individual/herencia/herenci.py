'''La herencia en poo(programacion orientada a objetos) es muy importantepermite la creación de clases
 nuevas basadas en clases existentes. La herencia establece una relación jerárquica entre las clases,
   donde una clase nueva (llamada "clase derivada" o "subclase") puede heredar atributos y métodos de 
   una clase existente (llamada "clase base" o "superclase").

class ClaseBase:
    # Definición de atributos y métodos de la clase base

class ClaseDerivada(ClaseBase):
    # Definición de atributos y métodos adicionales o modificados en la clase derivada
'''

class Animal:
    '''
    clase principal que describe nombre del animal
    '''
    def __init__(self, nombre):
        '''
        Constructor de la clase animal, recibe como argumentos el nombre del animal
        '''
        self.nombre = nombre
    
    def hacer_sonido(self):
        '''
        este método indica que el animal hace un sonido cualquiera.
        '''
        print("El animal hace un sonido.")

class Perro(Animal):
    '''
    clase que describe a perro como derivada de la clase animal y ademas de recibir el 'nombre' 
    recibe como argumento la raza de el perro.
    '''
    def __init__(self, nombre, raza):
        '''
        Este método usa el constructor de la clase inicial Animal y se modifica agregandole que reciba como argumentos
        nombre y raza, este ultimo fue el agregado al constructor original.
        '''
        super().__init__(nombre)
        self.raza = raza
    #    La llamada super().__init__(nombre) en el ejemplo se refiere a la invocación del constructoR...
    #    ...de la clase base dentro del constructor de la clase derivada. Permite inicializar los
    #    ...atributos  heredados de la clase base antes de agregar nuevos atributos específicos de la... 
    #    ...clase derivada.

    def hacer_sonido(self):
        '''
        hace referencia a que el perro que subclase de Animal hace un sonido, especificamente ladra.
        '''
        print("El perro ladra.")

class Gato(Animal):
    '''
    clase que describe a gato como derivada de la clase animal y ademas de recibir el 'nombre' 
    recibe como argumento la raza de el gato.
    '''
    def __init__(self, nombre, color):
        '''
        Este método usa el constructor de la clase inicial Animal y se modifica agregandole que reciba como argumentos
        nombre y color, este ultimo fue el agregado al constructor original.
        '''
        super().__init__(nombre)
        self.color = color
    
    def hacer_sonido(self):
        '''
        hace referencia a que el gato que subclase de Animal hace un sonido, especificamente maulla.
        '''
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
