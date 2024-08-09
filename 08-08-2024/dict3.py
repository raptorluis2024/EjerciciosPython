import random
curso ={ "rut1": "1-1", "notas1":[1,5.5,7],
         "rut2": "2-2", "notas2":[4,4.5,6.6],
         "rut3": "3-3", "notas3":[5,1.5,3.9,5.9],
         "rut4": "4-4", "notas4":[random.randrange(1,7) for x in range(4)]
    
}
print(curso)
#calcular el promedio del alumno3
print(curso["notas4"], sum(curso["notas4"])/len(curso["notas4"]))
