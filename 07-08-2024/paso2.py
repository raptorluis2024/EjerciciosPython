"""
Obtener otra lista con todas las palabras reversadas de la lista
original siempre y cuando la palabra tenga al menos 5 caracteres

"""
lista=[]
while True:
    palabra = input("Ingrese una palabra ")
    if len(palabra) == 0:
        print("no puede ser una palabra en blanco")
    else:
        lista.append(palabra)
    sigue = input("sigue s/n ").upper()
    if sigue != "S":
        break
lista2 = [x[::-1] for x in lista if len(x) > 5]
## lista2 = [x[::-1] if len(x) > 5 else x for x in lista ]
print(lista2)

lista3 = []
for pal in lista:
    if len(pal) > 5:
        lista3.append(pal[::-1])
    else:
        lista3.append(pal)
print(lista3)