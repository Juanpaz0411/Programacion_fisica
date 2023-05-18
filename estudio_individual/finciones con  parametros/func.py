'''
las funciones se pueden definir con y sin argumentos.
los argumentos son parametros por los que pasamos valores a la funcion.
requisito: los argumentos se pasan en el orden en el que estan definidos.

def saludar(saludo, nombre):
    print("digo", saludo, "a", nombre)

    saludar('hola', 'Juan')

imprime: 'digo hola a juan'
'''


def saludar(saludo, nombre):
    print("digo", saludo, "a", nombre)

saludar(saludo = 'hola', nombre = 'Juan')#de esta forma no importa el orden

#siempre hay que pasar todos los argumentos que tiene la funcion. hay una manera en que se puede escribir funciones 
#en forma que algunos argumentos sean opcionales, dandole valores por defecto a las funciones

def saludar(nombre, saludo = 'buenos dias'):#saludo se volvio opcional, los argumentossin valor por defecto van antes, con valor por defecto van despues.
    print("digo", saludo, "a", nombre)

saludar(nombre = 'juan')