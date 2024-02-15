from exercici27 import sumar_numeros

try:
    # Solicitar dos numeros
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))

    # Mostrar resultado
    resultado = sumar_numeros(num1, num2)
    print(f"La suma de {num1} y {num2} es: {resultado}")

except ValueError:
    print("Error: Introduce caracteres validos.")
