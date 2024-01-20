# main.py
from exercici33 import calcular_compra

def main():
    try:
        # Crear compra
        lista_compra = {100: 10, 250: 5, 1500: 30}
        # Solicitar IVA 
        iva = float(input("Introduce el porcentaje de IVA a aplicar: "))

        # Llamar función 
        calcular_compra(lista_compra, iva)

    except ValueError:
        print("Error: Ingresa un valor numérico válido para el IVA.")

if __name__ == "__main__":
    main()
