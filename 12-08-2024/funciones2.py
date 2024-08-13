import random
lista = [random.randrange(1,20) for x in range(10)]

def menu():
    print("\n1. Ingresar un elemento a la lista")
    print("2. Mostrar la lista")
    print("3. Mostrar promedio")
    print("4. Mostrar números pares")
    print("5. Mostrar números impares")
    print("6. Buscar un elemento ")
    print("7. Salir")
    opc = int(input("Escoja una opción :"))
    return opc

def ingresar():
    n = int(input("Ingrese un valor "))
    if n not in lista:
        lista.append(n)
    else:
        print("el número ya existe.")
    
def mostrar_lista():
    print("los elementos de la lista son " )
    for x in lista:
        print(x,",", end=" ")
 
def mostrar_promedio():
    return round(sum(lista)/len(lista),2)  

def mostrar_pares():
    print("los elementos pares de la lista son " )
    for x in lista:
        print(x if x%2==0 else "",",", end=" ")

def mostrar_impares():
    print("los elementos impares de la lista son " )
    for x in lista:
        print(x if x%2!=0 else "",",", end=" ")     

def buscar_elemento():
      n = int(input("Ingrese el valor a buscar "))
      if n in lista:
          print(f"el número {n} está en la posición {lista.index(n)}")
      else:
          print("El valor no está en la lista")   
           
while True:
    opcion = menu()
    if opcion == 1:
        ingresar()
    elif opcion == 2:
        mostrar_lista()
    elif opcion == 3:
        print(mostrar_promedio())
    elif opcion == 4:
        mostrar_pares()
    elif opcion == 5:
        mostrar_impares()
    elif opcion == 6:
        buscar_elemento()
    else:
        break
    
    