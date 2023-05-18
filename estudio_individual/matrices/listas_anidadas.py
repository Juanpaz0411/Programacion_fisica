#las listas anidadas son listas que estan dentro de otras listas ejemplo:

numeros = [[1, 2, 3], [4, 5, 6], 5, 6, 'perro', 13]

print(numeros)
'''
print(numeros[0],'y', numeros[4], 'son elementos de "NUMEROS"')

for i in numeros: 
    print(i)

#tambien hay ciclos anidados
'''
for j in numeros:#j es la fila o elemento
    if isinstance(j, list):#verifica si j es una lista
        for h in j:#para cada elemento h en fila j(si es una lista imprima)
            print(h)
    else:
        print(j) # sino, imprima j(elemento, ya que el for verifica la lsita)