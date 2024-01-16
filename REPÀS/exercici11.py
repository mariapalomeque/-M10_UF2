# Solicitar un numero entre 10 y 100
num = int(input("Introduce un número entre 10 y 100: "))

# Validar la entrada del usuario
if 10 <= num <= 100:
    # Creamos la  tupla 
    nums_tupla = tuple(range(1, num + 1))

    # Mostrar tupla 
    print("Tupla del 1 al", num, ":", nums_tupla)
else:
    print("Número no válido")
