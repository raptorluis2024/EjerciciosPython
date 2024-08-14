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

def multi(lista,n):
    posicion =0
    for x in range(len(lista)):
        lista[posicion] =   lista[posicion] * n 
        posicion += 1
    return lista
lista = [random.randrange(1,20) for x in range(10)]
print(lista)
print(multi(lista,8))
print(multi(8,lista))  ## genera error porque 8 no es iterable


    