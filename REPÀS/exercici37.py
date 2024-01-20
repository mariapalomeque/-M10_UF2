'''
# Codigo incorrecto:
ftotal = input('Introdueix el preu de tot el carrito: ')

# Llamala funcion antes de crearla
print(amb_iva(ftotal, iva))

def amb_iva(ftotal, iva = 21):
    #multiplicacion mal formulada
    ftotal = ftotal * iva  
    return ftotal 
'''
# Codigo corregido
ftotal = float(input('Introdueix el preu de tot el carrito: '))

def amb_iva(ftotal, iva=21):
    ftotal = ftotal * (1 + iva / 100)  
    return ftotal

print(amb_iva(ftotal))  
