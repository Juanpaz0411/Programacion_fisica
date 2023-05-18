
# def unafuncion(arg1, arg2, arg3, arg4):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#     print(arg4)



# def unafuncion(*args):#<*>ampaquing en una tupla
#     print(args)
# unafuncion('hola', 'y', 'o', 'u')
#toma todos los argumentos y los argumentos que toma la funcion los agrupa en una tupla
# se le pueden agregar infinidad de argumentos


# def unafuncion(*args):#toma los argumentos y los almacena en args
#     for i in args:
#         print(i)
# unafuncion('hola', 'y', 'o', 'u')#usando ciclos for se imprimen los valores

# def unafuncion(*args):
#     total = sum(args)
#     print(total)

# unafuncion(1,2,3,4,5,6,7,8,9,10)


# **kwargs

# def empleado(nombre, puesto, lenguaje):
#      print(nombre)
#      print(puesto)
#      print(lenguaje)

# empleado(nombre='carlos', puesto='programador', lenguaje='java') #kwargs arguments, ser especificos con la variable usada

def empleado(**kwargs):#<**>ampaquing en un diccionario
    for key, value in kwargs.items():
        print(f'{key}: {value}')

empleado(nombre='carlos', puesto='programador', lenguaje='java')

#kwargs.items() se utiliza para obtener una lista de pares clave-valor en el diccionario kwargs.


def expediente(**kwards):
    print(kwards)
    media=0
    for key in kwards:
        print(key, ':', kwards[key])#kwards[key], clave correspondient a la llave
        media += kwards[key]#media = media + kwards[key]
        print(media)
    print('media: ', media/ len(kwards))

expediente(HISTORIA=10, INGLES=2, MATEMATICAS=3)






