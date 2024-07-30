plata = int(input("Ingrese su bolsa de dinero "))
while plata > 0:
    gasto = int(input("Ingresa tu gasto"))
    #plata = plata - gasto
    if gasto <= plata:
        plata -= gasto
        print(f"gastaste {gasto} y te queda {plata}")
    else:
        print("saldo insuficiente")