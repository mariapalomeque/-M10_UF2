from exercici35 import comptar_paraules

try:
    # Solicitar frase
    frase_usuari = input("Introduce una frase: ")

    #Llamar funcion
    resultat = comptar_paraules(frase_usuari)

    # Mostrar diccionario 
    print("Diccionario:", resultat)

except ValueError:
    print("Error.")