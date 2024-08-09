"""calculo de notas usando una lista de diccionarios"""

curso =[]
curso.append({"rut":"1-1","n1":1.0, "n2":5.5, "n3":7})
curso.append({"rut":"2-2","n1":4.0, "n2":4.5, "n3":6.6})
curso.append({"rut":"3-3","n1":5.0, "n2":1.5, "n3":3.9})
final=0
print(curso)
for a in curso:
    final += a["n1"] + a["n2"] + a["n3"]
    a["promedio"] = final / 3
    if a["promedio"] >= 3.95:
        a["estado"] = "A"
    else:
        a["estado"] = "R"
    final = 0
    
print(curso)
curso[2]["n2"] = 4.1

for a in curso:
    final += a["n1"] + a["n2"] + a["n3"]
    a["promedio"] = final / 3
    if a["promedio"] >= 3.95:
        a["estado"] = "A"
    else:
        a["estado"] = "R"
    final = 0
print(curso)
#print(curso[0]["rut"])
"""
for a in curso:
    print(a,type(a))
    if "2-2" in a.values():
        print("ok")
    else:
        print("no tá")
"""
### calcular el promedio de cada alumno e indicar su estado final

    

