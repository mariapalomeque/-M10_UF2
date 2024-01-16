# Solicitar 10 numeros
entrada = input("Introduce 10 numeros separados por un espacio: ")

# Convertir en una lista de números y ordenarla
nums = list(map(int, entrada.split()))

# Solo funciona si introduces 10 numeros
if len(nums) == 10:
    # Crear una tupla con los números e ordenarla
    tupla_nums = tuple(sorted(nums))

    # Mostrar numeros ordenados
    print("Tupla ordenada:", tupla_nums)
else:
    print("Debes introducir exactamente 10 numeros.")
