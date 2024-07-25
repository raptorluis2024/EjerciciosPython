"""
El programa debe calcular f(x) = 3X**2 + 2x -1
"""
import math 
print("fx() = 3X**2 + 2x -1")
x = int(input("Ingrese valor de X :"))
fx = 3*math.pow(x,2) + 2*x -1 
print(f"El resultado para fx() = 3X**2 + 2x -1 con x={x} es {fx}")