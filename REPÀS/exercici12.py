# Creamos tupla  meses del año
meses = ("", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    # Solicitar numero del 0 al 12
    num = int(input("Introduce un numero del 0 al 12 (0 para salir): "))
    
    #Permitimos al usuario salir
    if num == 0:
        print("Programa finalizado.")
        break
    

    if 1 <= num <= 12:
        # Mostrar el mes 
        print("El mes", num, "es", meses[num])
    else:
        print("Numero no vàlid")
