'''
Dados los lados A y B de un triángulo rectángulo, según el Teorema de Pitágoras, el cuadrado de la hipotenusa (C), 
es igual a la suma del cuadrado de los catetos (lados).
c^2 = a^2 + b^2
Elaborar un programa que lea el tamaño de los lados A y B, y calcule e imprima C (hipotenusa)
'''

import math

catA = float(input("Ingrese medida cateto A: "))
catB = float(input("Ingrese medida cateto B: "))

hipotenusa = math.pow(catA,2) + math.pow(catB,2)
hipotenusa = round(math.sqrt(hipotenusa),2)

#hipotenusa =  math.sqrt(math.pow(catA,2) + math.pow(catB,2))
print(f"""La hipotenusa para un triangulo de cateto {catA}
y cateto {catB} = {hipotenusa}
      """)

