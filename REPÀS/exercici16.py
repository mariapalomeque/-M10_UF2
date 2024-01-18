# Solicitar una frase
frase = input("Introduce una frase: ")

# Crear  tupla (sin espacios)
tupla = tuple(frase.replace(" ", ""))

# Mostrar frase sin espacios
print("Tupla de caracteres (sin espacios):", ''.join(tupla))
