"""
notas=[]
for i in range(int(input("ingrese la cantidad de elementos"))):
    x = float(input("Ingrese una nota "))
    notas.append(x)
print(notas, min(notas), max(notas))    

notas.append("efsdfsdfs")
print(notas, min(notas), max(notas))    """
lista = [x**3 for x in range(8)]
print(lista)