from exercici35 import comptar_paraules

def main():
    try:
        # Solicitar frase
        frase_usuari = input("Introduce una frase: ")

        #Llamar funcion
        resultat = comptar_paraules(frase_usuari)

        # Mostrar diccionario 
        print("Diccionario:", resultat)

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
