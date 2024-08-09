curso ={ "1-1":[1,5.5,7],
         "2-2":[4,4.5,6.6],
         "3-3":[5,1.5,3.9,5.9]
        }
print("notas del curso")
for k,v in curso.items():
    print(k,v)
    
while True:
    rut = input("Ingrese el rut al que desea agregar una nota: ")
    if rut not in curso.keys():
        print("El rut no existe")
    else:
        nota = float(input("Ingrese la nota : "))
        curso[rut].append(nota)
    sigue = input("Desea continuar s/n").upper()
    if sigue != "S":
        break

for k,v in curso.items():
      
    print(f"""El rut {k} tiene {v} notas el promedio es {sum(v)/len(v):.2f} y su situación final es {'aprobado' if sum(v)/len(v) >= 3.95  else 'reprobado'}""")