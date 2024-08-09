curso ={ "1-1":[1,5.5,7],
         "2-2":[4,4.5,6.6],
         "3-3":[5,1.5,3.9,5.9]
        }

for k,v in curso.items():
      
    print(f"""El rut {k} tiene {v} notas el promedio es {sum(v)/len(v):.2f} y su situación final es {'aprobado' if sum(v)/len(v) >= 3.95  else 'reprobado'}""")
    
print("mejorando el promedio \n")
for notas in curso.values():
    notas[notas.index(min(notas))] = round(sum(notas)/len(notas),2)
print(curso)
curso["1-1"].append(4.8)
print(curso)

for v in curso.values():
    print(v)

    