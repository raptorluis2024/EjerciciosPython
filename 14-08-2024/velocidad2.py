import random
velocidad = [random.randrange(1,25) for x in range(60)]



def promedio(lista):
    return sum(lista)/len(lista)

print(velocidad,"\n", promedio(velocidad), "\n")

""" ARREGLAR """
## Se corrige la línea 19, cada vez que el elemento cumple se guarda la posición que en este caso
## corresponde al contador

def filtro_manual():
    promedio_vel = promedio(velocidad)
    resultado = []
    contador = 0
    for x in velocidad:
        if x > promedio_vel:
            resultado.append(contador)
        contador += 1
    return resultado
            
def filtro_2():
    promedio_vel = promedio(velocidad)
    resultado = []
    for pos, v in enumerate(velocidad):
        if v > promedio_vel:
            resultado.append(pos)
    return resultado

def filtro():
    promedio_vel = promedio(velocidad)
    return [x for x, v in enumerate(velocidad) if v > promedio_vel]

print(filtro())
print(filtro_manual())
print(filtro_2())