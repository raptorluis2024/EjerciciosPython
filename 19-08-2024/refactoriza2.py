def cuadrado_cubo(valor):
    return valor**2 + valor**3

def mult_234(valor):
    return valor*2 + valor*3 + valor*4

def op_combinada(valor):
    var_intermedia = cuadrado_cubo(valor)
    return mult_234(var_intermedia)

def compose(f, n):
    def fn(x):
        for _ in range(n):
            x = f(x)
        return x
    return fn

valor_entrada = 10
valor_6 = compose(op_combinada, 3)(valor_entrada)
print(valor_6)