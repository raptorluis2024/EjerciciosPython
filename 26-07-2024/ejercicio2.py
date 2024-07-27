"""
Una panadería vende (H)allullas, (M)arraquetas, pan (P)ita e (I)ntegral
El kilo de cada uno es 1990, 2010 , 2500 y 2600 respectivamente
El programa debe solicitar al usuario la cantidad en gramos de pan que quiere llevar
y su tipo.
Hoy la panaderia tiene una promomción, por cada 3 Kilos de pan, se regala un alfajor.
(Excepto por compra de pan integral)

Cuando el programa finalice se debe indicar los datos de entrada, salida e indicar 
si el cliente obtuvo o no de regalo uno o más alfajores
"""

pan = input("Ingrese pan H allulas M arraqueta P ita I ntegral : ")
peso = float(input("Ingrese el peso en gramos "))
alfajores = 0
if pan.upper() == "H":
    valor = 1990
elif pan.upper() == "M":
    valor = 2010
elif pan.upper() == "P":
    valor = 2500
else:
    valor = 2600
    
pago = valor*peso/1000
if pan.upper() != "I":
    alfajores = int((peso/1000)//3)
print(f"""Pan comprado {pan.upper()} precio por kilo ${valor}
      kilos {peso/1000:.3f} kg
      precio a pagar ${pago}  alfajores {alfajores}
      """)