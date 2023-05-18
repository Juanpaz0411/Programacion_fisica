"""
primero='ana'
segunda='jorge'
tercero='juan'
cuarta='paz'

print('llego 1', primero)
print('llego 2', segunda)
print('llego 3', tercero)
print('llego 4', cuarta)

es posible agrupar datos en estructuras de datos. 
""" 
'''estructura secuencial => conjunto de datos con un orden 
especifico, como el mismo tipo o longitud fija.
    se define entre 'corchetes'

1.list          -5 -4 -3 -2 -1
    numeros = [ 1, 2, 3, 4, 5]
                 0  1  2  3  4
    acceder a un elemento: 
        desde el inicio
            print(numeros[0])
        desde la cola
            print(numeros[-1])
        slicing, sacar un subconjunto de esos datos 
            print(numeros[0:4]) lista de 0-3, no incluye elemento 4
            print(numeros[0:4:2])lista en saltos de dos
'''

numeros = [ 1, 2, 3, 4, 5]

print(numeros[0])
print(numeros[-1])
print(numeros[0:4])
print(numeros[0:4:2])

lista1= [ 1, 2, 3]
lista2= [ 4, 5, 6]

print( lista1 + lista2 )#al sumar dos listas se concatenan
print(len(lista1))#es posible saber cuantos elementos hay con "len"
print(4 in lista1)#nos dice si un elemto esta dentro de ella "in"
print(3 in lista1 )