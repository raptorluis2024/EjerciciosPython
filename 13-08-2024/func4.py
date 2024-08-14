"""
argumentos posicionales y keyword-arguments

"""
""" crear una funcion que reciba 1 lista y un número 
debe retornar la lista actualizada para cada elemento como 
x*y
"""
import random
def multiplicar_lista(lista, n):
    return [x*n for x in lista]

def multi(lista=[1],n=1):
    posicion =0
    for x in range(len(lista)):
        lista[posicion] =   lista[posicion] * n 
        posicion += 1
    return lista
lista = [random.randrange(1,20) for x in range(10)]
print(lista)
#print(multi(lista,8))
print(multi(n=8,lista=lista))  
print(multi(lista=lista))
print(multi())
print(multi(lista=lista,n=5))  
print("1","2", sep="?",end="->")
print("3","4")