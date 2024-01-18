# Solicitar dos palabras
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

# Crear una tupla con las dos palabras
tupla = (palabra1, palabra2)

# Inicializar un diccionario para contar las veces que aparece cada caracter
n = {}

# Contar las apariciones de cada letra en ambas palabras
for palabra in tupla:
    for letra in palabra:
        if letra.isalpha():  
            # Ignorar caracteres que no son letras
            n[letra] = n.get(letra, 0) + 1

# Mostrar numero apariciones de cada letra
for letra, apariciones in n.items():
    print(f"{letra}: {apariciones}")
