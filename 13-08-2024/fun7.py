lista_numeros = [1,2,3,4,5]
lista_string = ['a','b','c','d','e']
def sumar_contar_tipos(lista,funcion):
    tipos = [type(elemento) for elemento in lista]
    opcion = funcion(lista)
    return tipos, opcion
tipo, conteo = sumar_contar_tipos(lista_string, len)
print(tipo)
print(conteo)
tipo, suma = sumar_contar_tipos(lista_numeros, sum)
print(tipo)
print(suma)