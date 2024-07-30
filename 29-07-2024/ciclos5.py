r="S"
saldo = 1000
veces=0
while r=="S":
    abono = int(input("Ingresa el valor del abono "))
    saldo += abono ##acumulando
    veces += 1 ## contar
    r = input("Quiere continuar s/n").upper()
print(f"saldo es {saldo} y abonaste {veces}  veces")
    