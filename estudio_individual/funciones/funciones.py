'''son basicas para entender como extraer la logica que 
queremos aplicar y separarla de los datos a los que se le 
aplicara

suma= 7 + 8 + 9
media= suma/3
print("la puntuacion de esta clase es", media)

en procesos repetidos es posible realizar funciones para 
aplicar en un conjunto de datos

las funciones siemprte tiene
    1 nombre
    2 argumentos de los que puede dependes(opcional)
    3 resultado
''' 
#escribimos funciones asi:
def puntuacion(alumno1, alumno2, alumno3):#los argumentos pueden ser nulos, pero siempre van parentesis.
    suma = alumno1 + alumno2 + alumno3 #definimos que hace nuestra funcion
    media = suma / 3
    return media #devolver el resultado de la funcion
''' la identacion nos dice que las lineas de codigo son parte
de la funcion'''

media = puntuacion( 7, 8, 9)
print("la puntuacion de esta clase es ", media)

media1 = puntuacion(3, 4, 5)
print("la puntuacion de la clase es ", media1)

'''el numero de argumentos puede ser aumentado usando las 
listas.'''
def punt(clase):
    med= sum(clase) / len(clase)#sum es la suma de los elementos de una lista
    return med
clase = [1, 2, 3, 4, 5, 6, 7, 8, 1]
media2 = punt(clase)

print("la puntuacion de la segunda clase es: ", media2)


