# Solicitar 10 numeros 
entrada = input("Introduce 10 numeros separados por un espacio: ")

# Convertir en una lista de numeros
numeros = list(map(float, entrada.split()))

# Solo funciona si introduces 10 numeros
if len(numeros) == 10:
    # Calcular la suma 
    suma = sum(numeros)
    # Calcular la media 
    media = suma / len(numeros)

    # Agregar la suma y la media a la lista
    numeros.extend([suma, media])

    # Mostrar la lista, la suma total y la media
    print(numeros)
    print("Suma total:", suma)
    print("Media:", media)
else:
    print("Debes introducir exactamente 10 números.")
