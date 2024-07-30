diccionario = {"Nombre": "Carlos",
"Apellido": "Santana",
"Ocupación": "Guitarrista"}
for clave, valor in diccionario.items():
    print(f"Mi {clave} es {valor}")
    
print(diccionario.items())

texto = input("Ingrese texto ")
for pos, letra in enumerate(texto):
    print(f"La letra en la posición {pos} es la {letra}")
    
for x in texto:
    print(x)