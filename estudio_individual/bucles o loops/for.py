'''
una repeticion de codigo o un bucle for, es la estructura de codigo que cambia el flujo de
ejecucion.
lo ciclos dados por los condicionales bifurcan el codigo, ya no es una sola linea de 
ejecucion sino que depende de las condiciones al ejecutar el codigo.

python utiliza el protocolo de iterador.

Iterar en Python significa recorrer un objeto iterable (como una lista, tupla, 
diccionario, conjunto, etc.) y realizar una operación en cada uno de sus elementos.

iterables en py: listas, Sets, tuple, diccionarios.

un blucle for en python es asi

for variable in iterable:
    print('inicio de iteracion')
    print(variable)
    print('fin iteracion')
'''
#lista
nombres = ['ana', 'Juan', 'roberto']
print('el tipo de nombres es', type(nombres))
for i in nombres:
    print('buenas dias', i)    

#tuple
nombres = ('ana', 'Juan', 'roberto')
print('el tipo de nombres es', type(nombres))
for nombre in nombres:
    print('buenas dias', nombre)    

#set, en esta estructura de datos los elementos no se mantienen el el mismo orden
nombres = {'ana', 'Juan', 'roberto'}
print('el tipo de nombres es', type(nombres))
for nombre in nombres:
    print('buenas dias', nombre) 

#diccionario
nombres = {'ana': 1, 'Juan': 2, 'roberto': 3}
print('el tipo de nombres es', type(nombres))
for nombre in nombres:
    print('buenas dias', nombre) 

#diccionario
nombres = {'ana': 1, 'Juan': 2, 'roberto': 3}
print('el tipo de nombres es', type(nombres))
for nombre in nombres:
    print('buenas dias', nombre, nombres[nombre])

#diccionario
nombres = {'ana': 1, 'Juan': 2, 'roberto': 3}
print('el tipo de nombres es', type(nombres))
for nombre, valor in nombres.items():
    print('buenas dias', nombre, valor)