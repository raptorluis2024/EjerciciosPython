dic ={}
while True:
    elemento = input("indique elemento ")
    precio = int(input("indique precio"))
    if elemento not in dic.keys():
        dic[elemento] = precio
    else:
        print("clave ya existe")
    resp = input("sigue s/n").lower()
    if resp != "s":
        break
print(dic)
for k in dic.keys():
    print(k)
    
for v in dic.values():
    print(v)
    
for k,v in dic.items():
    print(k,v)