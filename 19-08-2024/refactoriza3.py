import random
def promedio(notas):
    return sum(notas)/len(notas)

promedios=[]

def promedio_intermedio(dic):
    global promedios
    for v in dic.values():
        promedios.append(promedio(v))
    return promedio(promedios)
    
    
cursos={"C1":[random.randrange(1,7) for x in range(3)],
        "C2":[random.randrange(1,7) for x in range(3)],
        "C3":[random.randrange(1,7) for x in range(3)]}

print(cursos)
for k,v in cursos.items():
    print(f"el curso {k} tiene promedio {promedio(v):.2f}")
print(f"El promedio del colegio es {promedio_intermedio(cursos):.2f}")