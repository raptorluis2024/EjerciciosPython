"""
Generar una lista con la cantidad de letras que tiene cada palabra
de otra lista. El usuario ingresa las palabras a la lista original
y decide cuando terminar
"""
"""
lista = ["hola", "pala", "ala", "viento"]
lista2 = [] 
"""
lista=[]
lista2=[]
while True:
    palabra = input("Ingrese una palabra ")
    if len(palabra) == 0:
        print("no puede ser una palabra en blanco")
    else:
        lista.append(palabra)
    sigue = input("sigue s/n ").upper()
    if sigue != "S":
        break
print(lista)
lista2 = [len(x) for x in lista]
lista3=[]
for x in lista:
    lista3.append(len(x))
print(lista2)

