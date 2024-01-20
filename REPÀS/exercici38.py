'''
# Codigo incorrecto:
contactes = {'Roger': 678232311, 'Oriol': 566879326}

def elimina(contactes, user):
    # se elimina el contacto sin verificar si existe
    del contactes[user]
    #intenta emplear el contacto ya eliminado
    return contactes[user]
print(elimina(contactes, 'Pablo'))
'''

# Codigo corregido:
contactes = {'Roger': 678232311, 'Oriol': 566879326}

def elimina(contactes, user):
    if user in contactes:
        del contactes[user]
    return contactes  
print(elimina(contactes, 'Pablo'))
