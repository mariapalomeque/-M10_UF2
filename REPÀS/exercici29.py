def mostrar_numeros_entre_dos(num1, num2):
    try:
        # Verificar que el primer numero no sea mayor que el segundo
        if num1 > num2:
            num1, num2 = num2, num1

        # Mostrar los numeros enteros entre ellos
        print(f"Numeros enteros entre {num1} y {num2}:")
        suma = 0
        for numero in range(num1 + 1, num2 ):
            print(numero)
            suma += numero

        # Mostrar suma 
        print(f"La suma de los numeros enteros es: {suma}")

    except ValueError:
        print("Error")
