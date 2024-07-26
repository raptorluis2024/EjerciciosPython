color = input("Ingrese color ")
peso = int(input("Ingrese peso"))

if color.lower() == "verde" and  peso >=1 and peso <50:
    print("ok")
elif color.lower() == "azul":
    print("paso")
elif color.lower() == "rojo" and peso >= 10 and peso <= 50:
    print("tamo")
else:
    print("error")