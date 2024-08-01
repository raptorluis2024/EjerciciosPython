lista = ['Lechugas', 'Tomates', 5, 10,
True, False, True, 'Papas',
5.1, 45.2, 1, 2, 0]
count_str = 0
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
print(count_str)

lista_n = [elemento for elemento in lista if type(elemento) is str ]
print(lista_n, len(lista_n))