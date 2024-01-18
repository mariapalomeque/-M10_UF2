# Solicitar numeros hasta que ingrese 0
entrada_usuario = input("Introduce numeros separados por un espacio (termina con 0): ")

# Convertir una lista de números y ordenarla
nums = [int(num) for num in entrada_usuario.split() if num != '0']


if nums:
    # Crear una tupla con los números e ordenarla
    tuplas = tuple(sorted(nums))

    # Mostrar numeros ordenados
    print("Tupla ordenada:", tuplas)
else:
    print("No has ingresado ningun numero.")