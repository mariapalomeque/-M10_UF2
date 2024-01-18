diccionario_contactos = {}

while True:
    nombre = input("Introduce un nombre o fin para terminar: ")

    # Si el usuario introduce fin, termina
    if nombre.lower() == 'fin':
        break

    # Si el nombre ya consta en el diccionario no se agrega
    if nombre in diccionario_contactos:
        print(f"El nombre '{nombre}' ya esta en el diccionario. No se añadira.")
    else:
        # Solicitar edad 
        while True:
            edad_str = input(f"Introduce la edad de {nombre}: ")
            if edad_str.isdigit():
                edad = int(edad_str)
                diccionario_contactos[nombre] = edad
                break
            # Solicitar edad valida
            else:
                print("Introduce una edad valida (numero entero).")

# Imprimir  diccionario de contactos 
print("Contactos:")
for nombre, edad in diccionario_contactos.items():
    print(f"{nombre}: {edad} años")
