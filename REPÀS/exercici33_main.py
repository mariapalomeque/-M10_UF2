# main.py
from exercici33 import calcular_compra

try:
    # Crear compra
    lista_compra = {100: 10, 250: 5, 1500: 30}
    # Solicitar IVA 
    iva = float(input("Introduce el porcentaje de IVA a aplicar: "))

    # Llamar función 
    calcular_compra(lista_compra, iva)

except ValueError:
    print("Error.")
