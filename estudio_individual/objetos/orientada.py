
class Coche:#luego de esta linea se definen metodos y caracteristicas de la clase coche
    def __init__(self,marca, modelo):#Metodo que se encarga de crear una estancia de la clase(constructor __init__) métodos con dos barras bajas son métodos dunder.
        self.marca = marca#accedemos a la marca de self
        self.modelo = modelo#accedemos al modelo de self 
        self.arrancado = False #coche nuevo xd

    def arrancar(self):
        self.arrancar = True
        print("El", self.marca, self.modelo," se ha arrancado")

    def parar(self):
        self.parar = False
        print("El", self.marca, self.modelo, "se ha parado")

'''los métodos tienen un <self> este argumento hace referencia al objeto especifico que se esta creando, clase coche
una estancia viene dada por  un argumento self, tiene tantos argumentos como queramos<marca, modelo,...>
    nota: una estancia o instancia (en inglés "instance") es un objeto único creado a partir de una clase.

El método <__init__> es un método que python reconoce para CREAR UNA ESTANCIA.

al usar:
    self.marca = marca
    self.modelo = modelo
pasa el modelo y marca del constructor al modelo y marca del objeto.

de esta forma al usar 

laguna =Coche("renault", "Laguna") 
#self sera <laguna> y representa un objeto(estancia de clase coche) con las variables de la clase.
'''

laguna =Coche("renault", "Laguna")#( marca, modelo)
tesla = Coche("Tesla", "model 3")

print(type(laguna))
print(type(tesla))

print(laguna.marca, laguna.modelo)#se accede a las variables marca y modelo de las estancias con el <.>
print(tesla.marca, tesla.modelo)

laguna.arrancar()
tesla.arrancar()

print(laguna.arrancar)
print(tesla.arrancar)

laguna.parar()
tesla.parar()

print(laguna.parar)
print(tesla.parar)
