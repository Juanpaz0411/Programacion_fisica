
#una funcion con argumento a otra funcion es aceptable en cualquier lenguaje de programacion

def filtro_pares(numeros):
    resultado = []
    for i in numeros:
        if i % 2 == 0:
            resultado.append(i)
    return resultado

def filtro(numeros, condicion):
    resultado = []
    for i in numeros:
        if condicion(i):
            resultado.append(i)
    return resultado

def es_par(i):
    return i % 2 == 0

def es_positivo(i):
    return i > 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

print(filtro(numeros, es_par))
print(filtro(numeros, es_positivo))