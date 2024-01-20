'''
# Codigo incorrecto:

# uso de " en vez de dos '
passwd= input('Introdueix una contrasenya: ")

# uso in en vez de == y variable incorrecta 
if contrasenya  in ['Peliñ4nd0#'):
  print('Correcte')

#faltan :
else  
     print('Incorrecte')
'''


# Codigo corregido:

contrasenya = input('Introdueix una contrasenya: ')

if contrasenya == 'Peliñ4nd0#':
    print('Correcte')
else:  
    print('Incorrecte')