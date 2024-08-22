from vars import masas,salsas

def cambiarmasa(p,base):
    p["masa"] = masas[base]

def cambiarsalsa(p,salsa):
    p["salsa"] = salsas[salsa]

def agregar_ingrediente(p,i):
    if i not in p["ingredientes"]:
        p["ingredientes"].append(i)
        return True
    else:
        return False

def eliminar_ingrediente(p,i):
    if i in p["ingredientes"]:
        p["ingredientes"].pop(p["ingredientes"].index(i))
        return True
    else:
        return False



    