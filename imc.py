'''
Desarrollar un programa que permita obtener el IMC de una
persona a partir de su peso en kilogramos y su estatura en metros.
IMC =     peso
       ----------
        estatura^2
'''
import math as m

peso = float(input("Ingrese peso en Kg "))
estatura = float(input("Ingrese estatura en mt "))
imc = round(peso / (m.pow(estatura,2)),3)
print(f"""El IMC en base a un peso de {peso} kg y una estatura de 
      {estatura} mts es {imc}
""")

