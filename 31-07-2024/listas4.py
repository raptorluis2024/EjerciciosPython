a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)

filtro2 = [x for x in a if x >= 1000]
print(filtro2)

minutos = [120, 50, 600, 30, 90, 10, 200, 0, 500]
resultado = ["bien" if x < 90 else "mal" for x in minutos ]
print(resultado)