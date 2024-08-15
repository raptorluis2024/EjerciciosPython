import random
velocidad = [random.randrange(1,25) for x in range(60)]



def promedio(lista):
    return sum(lista)/len(lista)

print(velocidad,"\n", promedio(velocidad), "\n")

""" ARREGLAR *****"""
def filtro_manual():
    promedio_vel = promedio(velocidad)
    resultado = []
    contador = 0
    for x in velocidad:
        if x > promedio_vel:
            resultado.append(velocidad.index(velocidad[contador]))
        contador += 1
    return resultado
            
    
def filtro():
    promedio_vel = promedio(velocidad)
    return [x for x, v in enumerate(velocidad) if v > promedio_vel]

print(filtro())
print(filtro_manual())