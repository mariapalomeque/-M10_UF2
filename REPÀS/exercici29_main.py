from exercici29 import mostrar_numeros_entre_dos

try:
    num1 = int(input("Introduce el primer numero entero: "))
    num2 = int(input("Introduce el segundo numero entero: "))

    mostrar_numeros_entre_dos(num1, num2)

except ValueError:
    print("Error.")