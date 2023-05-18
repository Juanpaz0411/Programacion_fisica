'''
 si se cumple una condicion, habrá una consecuencia.(se inicia con la 
 condición y se sigue con la consecuencia).

cualquier condicion es algo que puede evaluarse como verdadero o falso.

la condicion es un booleano, si es falso o verdadero, la consecuencia
es lo que se hara dependiendo del booleano.

 -condicion 'si'
    ejemplo: <si> tienes la llave.=> false o True
    -consecuencia: 'puedes pasar o' no 'puedes pasar'
'''

tienes_llave = input('tienes una llave? ')#input imprime en pantalla y permite al usuario interactuar con el codigo

'''
if corresponde a 'si'
ejemplo
if condicion:
    primera orden
    segunda orden
    tercera orden
== es el operador de igualdad, da verdadero si a ambos lados son
iguales, falso si no lo son
'''
if tienes_llave == 'si':
    print('puedes pasar')#identado a la derecha de if
else:#en cualquier otro casi diferente del if
    print('no puedes pasar')

print('fin')#al no estar identado a a derecha de if no lo afecta el bool

'''
if condicion:
    ...
    ...
    ...
elif condicio_2:
    esto se ejecuta si no se cumple condicion pero se cumple condicion_2

'''

tienes_key = input('tienes key? ')
if tienes_key == 'si':
    forma = input('que forma tiene la llave ')
    color = input('que forma color la llave ')
    if forma == 'cuadrada' and color == 'naranja':
        print('puedes pasar')
    elif forma == 'redonda' and color == 'ámarillo':
        print('mereces entrar realmente? ')
    elif forma== 'triangular' and color == 'rosada':
        print('magnifico, pasa')
    else:
        print('estás como davivienda, en el lugar equivocado')
else:
    print('no puedes pasar mamahuevo. >:C')
