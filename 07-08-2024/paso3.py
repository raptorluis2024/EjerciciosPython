import random
lista = [random.randrange(1,20) for x in range(5)]
lista.reverse()
print(lista)
#palabra = "hola"
print(lista[2])
print(lista[1:2])
print(lista[1:3])
print(lista[2:4])
print(lista[::])
print(lista[3:1:-1])
tc = "7809777712223833757656757"  ## 7809
print(tc[0:4])
tc_x = tc[len(tc):len(tc)-5:-1]
print(tc_x[::-1])
pal = "hola"
print(pal, pal[::-1])
