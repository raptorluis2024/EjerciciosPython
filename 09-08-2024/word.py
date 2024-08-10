"""
import sys
archivo = sys.argv[1]

with open(archivo, "r") as file:
    texto=file.read()
print(texto)
"""
lista = ["hola", "como", "estas", "como", "te", "va"]
print(set(lista))

lorem = """
Curabitur facilisis eleifend sapien, nec suscipit magna euismod quis. Integer dolor dui, consequat vel ullamcorper eu, maximus vitae leo. Proin eu mi rutrum, lacinia purus in, cursus turpis. Maecenas commodo arcu nunc, et ornare nunc luctus sed. Proin scelerisque ornare erat, vel porta urna sollicitudin a. Duis eleifend dolor orci, id vestibulum nunc vestibulum at. Praesent vel ligula elit.
"""
print(len(set(lorem)))
#lista = lorem.split(" ")
print(len(lorem.split(" ")), len(set(lorem.split(" "))))
lorem = lorem.replace(",","")
lorem = lorem.replace(".","")

print(lorem)
print(len(lorem.split(" ")), len(set(lorem.split(" "))))
