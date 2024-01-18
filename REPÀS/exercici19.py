areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

# Imprimir segundo elemento
print("Segundo elemento :", areas_pis[1])

# Imprimir ultimo elemento 
print("Ultimo elemento:", areas_pis[-1])

# Imprimir area terraza
print("Area de la terraza:", areas_pis[areas_pis.index("Terrassa") + 1])

# Imprimir del primer elemento al tercero
print("Del primer al tercer element:", areas_pis[:3])

# Imprimir del tercer al ultimo elemento
print("Del tercer elemento al ultimo:", areas_pis[2:])

# Imprimir area total de las dos habitaciones
area_habitaciones = areas_pis[areas_pis.index("Habitació1") + 1] + areas_pis[areas_pis.index("Habitació2") + 1]
print("Total àrea de les dues habitacions:", area_habitaciones)

# Modificar area baño, imprimir nueva lista
areas_pis[areas_pis.index("Lavabo") + 1] = 8.5
print("Nueva lista:", areas_pis)

# Añadir area patio interior, y imprimir nueva lista 
areas_pis.extend(["Pati interior", 2.78])
print("Nueva lista:", areas_pis)

# Imprimir area total piso
area_piso =sum(area for area in areas_pis[1:] if isinstance(area, (int, float)))
print("Area total piso:", area_piso)
