plata = int(input("Ingrese su bolsa de dinero "))
ganas ="S"
while plata > 0 and ganas == "S":
    gasto = int(input("Ingresa tu gasto"))
    #plata = plata - gasto
    if gasto <= plata and gasto%5000==0:
        plata -= gasto
        print(f"gastaste {gasto} y te queda {plata}")
    else:
        print("saldo insuficiente")
    ganas = input("tienes ganas de seguir gastando dinero s/n").upper()