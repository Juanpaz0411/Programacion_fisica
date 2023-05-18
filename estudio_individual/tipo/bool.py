'''
los datos de tipo bool guardan valores de verdadero y falso(true,false)
aqui hay operadores logicos, 'and' este devuelve verdadero su los
dos valores comparados son verdaderos, 'or' devuelve verdader si
uno de los dos valores comparados son verdaderos, 'not' aplicado
en datos bool devolviendo el OPUESTO.
'''
print("operador and")
print('true and true:', True and True)
print('true and false:', True and False)
print('false and true:',False and True)
print('false and false:', False and True)

print("operador or")
print('true and true:', True or True)
print('true and false:', True or False)
print('false and true:',False or True)
print('false and false:', False or True)

print("operador not")
print('true and true:', not True)
print('true and false:', not False)

'''existen operadores que se definen sobre tipos de datos no 
booleanos pero como resultado da un booleano.'''
print(10 > 5)
print(10 >= 5)
print(10 < 5)
print(10 <= 5)
print(10 == 5) #igual que
print(10 != 5) #diferente
