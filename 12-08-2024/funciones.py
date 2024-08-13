import random
lista = [random.randrange(1,20) for x in range(10)]

def menu():
    print("\n1. Ingresar un elemento a la lista")
    print("2. Mostrar la lista")
    print("3. Mostrar promedio")
    print("4. Salir")
    opc = int(input("Escoja una opción :"))
    return opc

def ingresar():
    n = int(input("Ingrese un valor "))
    lista.append(n)
    
def mostrar_lista():
    print("los elementos de la lista son " )
    for x in lista:
        print(x,",", end=" ")
 
def mostrar_promedio():
    return round(sum(lista)/len(lista),2)  
    
while True:
    opcion = menu()
    if opcion == 1:
        ingresar()
    elif opcion == 2:
        mostrar_lista()
    elif opcion == 3:
        print(mostrar_promedio())
    else:
        break
    
    