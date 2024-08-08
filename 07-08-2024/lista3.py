"""
lista=[x for x in range(5)]
lista.insert(44,2)
print(lista)

lista=[x for x in range(5)]
lista.insert(44,2)
lista.pop(3)
lista.append(44)
lista.sort()
lista2 = lista 
lista3 = lista[::]
lista4 = lista[3::-1]
"""
import random
lista2 = [ random.randrange(1,8) for x in range(10) ]
print(lista2)
if 7 in lista2:
    print(lista2.index(7))