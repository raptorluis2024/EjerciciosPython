def cuadrado_cubo(base):
    cuadrado = base**2
    cubo = base**3
    cuarta = base**4
    return cuadrado, cubo, cuarta
print(cuadrado_cubo(2),type(cuadrado_cubo(2)))
a,b,c = cuadrado_cubo(3)
print(a,b,c)
for x in cuadrado_cubo(3):
    print(x)