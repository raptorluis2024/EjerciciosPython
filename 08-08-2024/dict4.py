curso ={ "1-1":[1,5.5,7],
         "2-2":[4,4.5,6.6],
         "3-3":[5,1.5,3.9,5.9]
        }

for k,v in curso.items():
    promedio = sum(v)/len(v)
    if promedio >= 3.95:
        estado = "A"
    else:
        estado = "R"
        
    print(f"""El rut {k} tiene {v} notas el promedio es {promedio}
          y su situación final es {estado}""")
