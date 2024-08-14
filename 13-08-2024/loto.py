import random
pool = [n for n in range(1,42)]
ganador=[]


def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(f'El {posicion} es {elegido}')
    return elegido

for x in range(6):
    ganador.append(sacar_numero(x))
print(ganador)

juego=[]

for jugador in range(4):
    pool = [n for n in range(1,42)]
    loto =[]
    for x in range(1,7):
        loto.append(sacar_numero(x))
    juego.append(loto)
print(juego)

"""
[5, 22, 41, 33, 25, 35] ganador

[7, 18, 6, 41, 28, 5]
"""








"""
print(pool)
elegido = random.choice(pool)
print("El primer número es", elegido)
# sacamos el 2do, pero debemos evitar que se vuelva
# a sacar el número anterior
pool.remove(elegido)
elegido = random.choice(pool)
print("El segundo número es", elegido)
print(pool)
"""

