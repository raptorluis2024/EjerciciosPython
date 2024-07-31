"""
Generar un algoritmo que permita ingresar 10 números y mostrar el promedio de los números múltiplos de 3 ingresados
"""
"""numeros=0
suma=0
for x in range(10):
    n=int(input("Ingrese un numero "))
    if n%3==0:
        numeros+=1
        suma+=n
print(suma/numeros)       
"""     
"""
Generar un algoritmo que permita ingresar dos números.
Si el primer número es mayor que el segundo muestra la suma
Si son iguales muestra la multiplicación
Si el segundo es mayor que el primero muestra la tabla de
multiplicar de ese número
"""
"""
n1 = int(input("Ingrese primer valor"))
n2 = int(input("Ingrese segundo valor"))
if n1 > n2:
    print(n1+n2)
elif n1 == n2:
    print(n1*n2)
else:
    for x in range(1,11):
        print(f"{n2} *{x} = {n2*x}")
"""

"""
Generar un algoritmo que permita ingresar un número, debe ser mayor a 10.
En caso contrario escribe 5 veces la palabra error y vuelve a pedir el número.
El usuario decide cuando terminar.

"""

while True:
    num=int(input("Ingrese un numero"))
    
    if num<=10:
        for x in range(5):
            print("ERROR")
    else:
        print(f"Numero ingresado: {num} ")
        op=input("Desea continuar? S/N").upper()
        if op=='N':
            break