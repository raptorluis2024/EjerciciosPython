"""
lista_par = [2*i + 2 for i in range(int(input("x?")))]
print(lista_par)

string= "estamos aprendiendo python"
l1 =[letra for letra  in string]
print(l1)
"""
import random
#valores = [0,4,5,6,7,8,9]
valores=[int(random.random()*200) for x in range(7) ]
print(valores)

divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(divisibles)

div2 = ["divisible" if x%2==0 else "no divisible" for x in valores]
print(div2)

"""
Generar una lista con 10 números que sean multiplos de 5 o que sean mayores de 50, de lo contrario coloca 0
"""
valores=[int(random.random()*200) for x in range(10) ]
nueva_lista = [ x if x%5==0 or x > 50 else 0 for x in valores]
print(valores)
print(nueva_lista)


