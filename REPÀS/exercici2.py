# Solicitar  valor en €
valor_original = float(input("Introduce el valor en €: "))

# Solicitar  porcentaje de iva
porcentaje_iva = float(input("Introduce el porcentaje de IVA (4%, 10% o 21%): "))

# Calculo iva y precio final
iva = valor_original * (porcentaje_iva / 100)
valor_final = valor_original + iva

# Prints
print("Valor original:", valor_original, "€")
print("IVA (", porcentaje_iva, "%):", round(iva, 2), "€")
print("Valor final con IVA:", round(valor_final, 2), "€")
