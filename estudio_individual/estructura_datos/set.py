'''
un set es una estructura no secuencial, no importa el orden de
los elementos, no puede tener elementos duplicados

set1 = set([1, 2, 3, 4, 5, 6 , 7, 8, 9, 10])es un conjunto, se 
llama a la funcion con una lista que tiene los elementos que 
queremos en set


'''
set1 = set([1, 2, 3, 4, 5, 6 , 7, 8, 9, 10])
set2 = set([2, 4, 4, 4, 6, 6 , 8, 10, 12, 14, 16, 18])#quita los datos duplicados

print(set1)
print(set2)

print(set1-set2)#que elementos estan en set 1 que no en set 2
print(set2-set1)#los elementeos de set 2 que no estan en set 1
print(set1 & set2)#interseccion de los dos conjuntos
print(set2 | set1)#union, los elementos de ambos sets

