# Solicitar al usuario que introduzca dos palabras
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

# Verificamos que ambas palabras tengan mas de dos letras
if len(palabra1) >= 2 and len(palabra2) >= 2:
    # Intercambiar las dos primeras letras
    nueva_palabra1 = palabra2[:2] + palabra1[2:]
    nueva_palabra2 = palabra1[:2] + palabra2[2:]

    # Mostrar el resultado
    print(nueva_palabra1, nueva_palabra2)
 
else:
    print("Las palabras deben tener minimo dos letras")
