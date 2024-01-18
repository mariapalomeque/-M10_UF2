# Solicitar una frase
frase = input("Introduce una frase: ")

# Inicializar una cadena 
frase_final = ""

# Bucle elimina espacios y caracteres r 
for char in frase:
    if char not in frase_final and not char.isspace():
        frase_final += char

# Mostrar la frase final
print("Frase final:", frase_final)


