def cuadrado_cubo(valor):
    return valor**2 + valor**3

def mult_234(valor):
    return valor*2 + valor*3 + valor*4
valor_entrada = 2
valor_1 = cuadrado_cubo(valor_entrada)
print("valor_1", valor_1)
valor_2 = mult_234(valor_1)
print("valor_2", valor_2)
valor_3= cuadrado_cubo(valor_2)
print("valor_3", valor_3)
valor_4 = mult_234(valor_3)
print("valor_4", valor_4)
valor_5 = cuadrado_cubo(valor_4)
print("valor_5", valor_5)
valor_6 = mult_234(valor_5)
print(valor_6)
print(cuadrado_cubo(cuadrado_cubo(2)*mult_234(2)))