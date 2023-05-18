'''es una estructura... que tampoco es secuencial
es como una lista, a la que se le acceden a los elementos con
una 'key' o una palabra que lo identifica
    se define entre llaves {}
'''
#cada elemento es una pareja de palabra clave y valor
#{key:valor}
persona = {"nombre":"juan","edad": 30, "apellido": "lopez"}
#print(persona)
print(persona["nombre"])
print(persona["apellido"])
print(len(persona))
print("nombre" in persona)
print("juan" in persona)
print("edad" in persona )