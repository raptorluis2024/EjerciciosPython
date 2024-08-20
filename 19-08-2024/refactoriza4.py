import random
def promedio(notas):
    return sum(notas)/len(notas)

promedios=[]

def promedio_intermedio(dic):
    global promedios
    for v in dic.values():
        promedios.append(promedio(v))
    
   
cursos={"C1":[random.randrange(1,7) for x in range(3)],
        "C2":[random.randrange(1,7) for x in range(3)],
        "C3":[random.randrange(1,7) for x in range(3)]}

print(cursos)
promedio_intermedio(cursos)
for c in promedios:
    print(f" tiene promedio {c:.2f}")
print(f"el promedio del colegio es {promedio(promedios)}")
    
