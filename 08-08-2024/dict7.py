curso ={ "1-1":[],
         "2-2":[],
         "3-3":[]
        }
print("notas del curso")
for k,v in curso.items():
    print(k,v)
## no hay notas, se deben agregar máximo 3 notas por alumno
while True:
    rut = input("Ingrese el rut al que desea agregar una nota: ")
    if rut not in curso.keys():
        print("El rut no existe")
    elif len(curso[rut]) == 3:
        print("no puede ingresar más notas")
    else:
        nota = float(input("Ingrese la nota : "))
        curso[rut].append(nota)
    sigue = input("Desea continuar s/n").upper()
    if sigue != "S":
        break

for k,v in curso.items():
    if len(v) > 0:
        print(f"""El rut {k} tiene {v} notas el promedio es {sum(v)/len(v):.2f} y su situación final es {'aprobado' if sum(v)/len(v) >= 3.95  else 'reprobado'}""")
    else:
        print(f"alumno {k} no tiene notas")