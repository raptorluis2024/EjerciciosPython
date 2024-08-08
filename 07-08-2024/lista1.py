import random 
lista = [x for x in range(10)]
lista2 = [ random.randrange(1,50) for x in range(10) ]
print(lista,lista2)
#lista.extend(lista2)
#print(lista)

for a in lista2:
    lista.append(a)

print(lista)
if 35 in lista:
    lista.remove(35)
else:
    print("no ta")
print(lista)
#print(lista.contains(35))
lista.reverse()
print(lista)
lista.append("dsfsfdsf")
lista.append(1.1)
print(lista)
c=0
for i in lista:
    if type(i) is float:
        c+=1
print(c)