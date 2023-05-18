'''
es una coleccion o conjunto de elementos formado por filas y columnas, hay matrices uni,bi y tri-dimensionales.
'''

#matrix unidimensional - vertical
for i in range(1, 7):
    print(i)

#matrix unidimensional - horizontal
  

#matrix bidimencional(6x6) 
for i in range(1, 7):
    for j in range(1, 7):
        print(0, end = '  ')
    print(' ')

for i in range(1, 7):
    for j in range(1, 7):
        print(f'({i}, {j})' , end = ' ')
    print(' ')

'''La línea de código "print(f'({i}, {j})' , end = ' ')" usa f-strings (también conocido como formatted 
string literals) para imprimir una cadena de texto que muestra los valores de las variables i y j. 
El uso de f-strings permite que las variables i y j se inserten directamente en la cadena de texto 
mediante la sintaxis { } y se evalúen en tiempo de ejecución.'''