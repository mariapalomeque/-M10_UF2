# Solicitar al usuario un número del 1 al 10
num = int(input("Introduce un número del 1 al 10: "))


if 1 <= num <= 10:
    # Mostrar la tabla de multiplicar del número ingresado
    print("Tabla de multiplicar del", num, ":")
    for i in range(1, 11):
        result = num * i
        print(num, "x", i, "=", result)
else:
    print("Número no válido")