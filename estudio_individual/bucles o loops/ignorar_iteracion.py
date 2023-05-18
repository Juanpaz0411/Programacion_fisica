'''si hay un punto del codigo que no requiere ser ejecutado es posible saltar algunas 
partes del codigo, especificamente las iteraciones con el uso de <continue>

ejemplo
for tweet in tweets:
    print('antes')
    continue
    print('despues')

cualquier codigo antes de continue se ejecutara con normalidad, el codigo luego de continue
se salta el codigo restante abajo, vovliendoa la iteracion anterior.

for tweet in tweets:
    print('antes')
    if condicion:
        continue
        print('despues')
ejemplo:
    for tweet in tweets:
        if usuario != 'babel22'
            continue
        procesar(tweet)

si hay un punto a partir del cual no se quiere seguir leyendo puede parar la iteracion <break>

#se ejecuta todo antes de break, en break se salta del bucle, no se salta la siguiente
iteracion sino que se olvidan las iteraciones faltantes y sigue la ejecucion del codigo.
se ejecuta cuando se cumple una condición.

for tweet in tweets:
    print('antes')
    if condicion:
        break
    print('despues')

print('fuera del bucle')

como sabemos si hemos salido del bucle? usando <else>
else tambien es posible usarlo con un for o un while

for tweet in tweets:
    [...]
    if parar:
else:
    print('todos leidos')

while condicion:
    [...]
    if parar:
else:
    print('todos leidos')

#cualquier codigo dentro del else se ejecuta si se termino el bucle de forma natural es decir
si no se ha ejecutado un break dentro de el.

'''













