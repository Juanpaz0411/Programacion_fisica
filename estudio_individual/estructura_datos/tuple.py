'''
una tupla es parecida a una lista, pero esta es inmutable, no
es posible agregarle, quitarle o modificarle a sus elementos
    se accede al igual que en una lista
    se define entre 'parentesis'
'''

lista = [1, 2]
par = (1, 2)#tupla

print(par)
print(lista)

print(par[0])
print(lista[1])

lista[0] = 5#se le da al primer elemento el valor de 5
print(lista)

#par[0] = 5  hay un error, tuple no soporta diferentes valores...

