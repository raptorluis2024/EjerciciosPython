import random
def promedio(notas):
    return sum(notas)/len(notas)

promedios=[]

def promedio_intermedio(dic):
    global promedios
    for k,v in dic.items():
        promedios.append((k,promedio(v)))
    
   
cursos={"C1":[random.randrange(1,7) for x in range(3)],
        "C2":[random.randrange(1,7) for x in range(3)],
        "C3":[random.randrange(1,7) for x in range(3)]}

print(cursos)
promedio_intermedio(cursos)
for c in promedios:
    print(f"{c[0]} tiene promedio {c[1]:.2f}")
lista=[v for k,v in promedios]
#print(lista)
print(f"el promedio del colegio es {promedio(lista)}")
    
