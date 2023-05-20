#el programa fue realizado de forma grupal

def move_disk(n, source, target):
    print(f"Mueve el disco {n} de la torre {source} a la torre {target}")

def hanoi(n, source, target, auxiliary):
    if n == 1:
        move_disk(1, source, target)
    else:
        hanoi(n-1, source, auxiliary, target)
        move_disk(n, source, target)
        hanoi(n-1, auxiliary, target, source)

print("Torre de Hanoi")
while True:
    try:
        discos = int(input("¿Con cuántos discos quieres jugar? "))
        if discos <= 0:
            print("El número de discos debe ser mayor que cero")
        else:
            break
    except ValueError:
        print("Debe ingresar un número entero")

print(f"Comenzando el juego con {discos} discos")
print("Los movimientos a realizar son:")
hanoi(discos, "A", "C", "B")



