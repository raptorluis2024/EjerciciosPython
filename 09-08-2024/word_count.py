import sys
if len(sys.argv) > 1:
    archivo = sys.argv[1]
else:
    archivo = "lorem_ipsum.txt"
    
with open(archivo, "r") as file:    
    texto=file.read()

lista = texto.split(" ")
palabras = set(lista)
letras = set(texto)
print(f"""El número de caracteres distintos es : {len(letras)}
El número de palabras diferentes es: {len(palabras)}""")

test = [p.replace("a","") for p in palabras if len(p)>8]
print(test)
"""
print(len(texto))
texto = texto.replace(",","")
texto = texto.replace(".","")
texto = texto.replace("\n","")
print(len(texto))

print(texto)
print(len(set(texto.split(" "))))
"""
