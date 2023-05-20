def solicitar_edad():
    '''
    solicita al usuario la edad, si se ingresa un tipo de entrada diferente de entero se 
    personalizo la salida valueError.
    '''
    try:
        edad = int(input("\nPor favor, ingrese su edad: "))
        if edad == 13:
            print('aqui la tiene pa que me la bese.')
        return edad
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return solicitar_edad()

def solicitar_mes():
    '''
    solicita al usuario el mes, si se ingresa un tipo de entrada diferente de entero se 
    personalizo la salida valueError.
    '''
    try:
        mes = int(input("\nPor favor, ingrese su mes de nacimiento (en números): "))
        return mes
    except ValueError:
        print("\nError: Ingrese un número entero válido.")
        return solicitar_mes()

def mayoria_de_edad():
    '''
    funcion que a través de las funciones solicitar_edad y solicitar_mes dictamina si 
    el usuario es menor o mayor de edad, hay reestricciones para el uso del calendario 
    gregoriano.
    '''
    try:
        edad = solicitar_edad()
        if edad >= 0:
            mes = solicitar_mes()
            if mes <= 12 and mes > 0:
                if edad >= 18:
                    print("mayor de edad")
                else:
                    print("menor de edad")
            elif mes == 13:
                print('aqui la tiene pa que me la bese.\n \n \n Error, solo hay 12 meses')
            else:
                print("error, solo hay 12 meses")
        else:
            print("xd")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

mayoria_de_edad()
