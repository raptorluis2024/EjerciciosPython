from vars import masas,salsas,ingredientes

def menu_ingredientes():
    print("Escoja los ingredientes " )

    for x,y in enumerate(ingredientes):
        print(x,y)
    opc = int(input("Ingrese una opción : "))
    return opc 

def menu_masas():
    print("Escoja una de las masas " )
    for x,y in enumerate(masas):
        print(x,y)
    opc = int(input("Ingrese una opción : "))
    return opc 
    

def menu_salsas():
    print("Escoja una de las salsas")
    for x,y in enumerate(salsas):
        print(x,y)
    opc = int(input("Ingrese una opción : "))
    return opc 

def menu_principal():
   
    print("Escoja una opción")
    print("1. Seleccionar Base")
    print("2. Seleccionar Salsa")
    print("3. Agregar Ingrediente")
    print("4. Eliminar Ingrediente")
    print("5. Mostrar Pizza")
    print("6. Aceptar Pedido")
    print("7. Salir")
    opc = int(input("Ingrese una opción : "))
    return opc   

if __name__ == "__main__":
    menu_principal()      