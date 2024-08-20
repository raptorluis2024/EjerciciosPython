def cuadrado_cubo(valor):
    return valor**2 + valor**3

def mult_234(valor):
    return valor*2 + valor*3 + valor*4

def op_combinada(valor):
    var_intermedia = cuadrado_cubo(valor)
    return mult_234(var_intermedia)

valor_entrada = 10
valor_2 = op_combinada(valor_entrada)
valor_4 = op_combinada(valor_2)
valor_6= op_combinada(valor_4)
print(valor_2, valor_4, valor_6)