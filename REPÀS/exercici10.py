import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Crear variables
intentos = 0
adivinado = False

# Bucle hasta adivine el número
while not adivinado:
    # Solicitar  un número
    intento = int(input("Introduce un numero entre 1 y 100 : "))
    
    # Incrementar el contador de intentos
    intentos += 1
    
    # Verificar si el número es correcto
    if intento == numero_secreto:
        adivinado = True
        print(f"¡Felicidades! Adivinaste en {intentos} intentos.")
    else:
        # Indicar si es más pequeño o más grande
        if intento < numero_secreto:
            print("El numero es más grande. Intenta de nuevo.")
        else:
            print("El numero es más pequeño. Intenta de nuevo.")
