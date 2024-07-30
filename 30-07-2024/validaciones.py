"""
EL programa debe permitir el ingreso de 5 notas validadas en el rango
Se debe imprimir el promedio una vez que finalice el programa

v2.0 Indicar cuál fue la menor y la mayor nota ingresada durante el proceso

"""

import getpass
a = getpass.getpass()

while True:
    nota = float(input("Ingrese una nota "))
    if nota >= 1 and nota <= 7:
        print("Nota valida")
        break
    else:
        print("nota inválida")
        continue
