'''
Elaborar un programa que calcule e imprima el precio de venta de un artículo.
Se tienen los datos Descripción del artículo y costo de producción. 
El precio de venta se obtiene añadiendo al costo el 120% como utilidad 
y el 19% de impuesto.
'''
######## datos de entrada
descripcion = input("Ingrese nombre del articulo")
costo = int(input("Ingrese costo de producción " ))
######## proceso
precio_venta = costo *1.2 + costo*0.19
#############salida
print(f"""El precio de venta del producto {descripcion}
      con precio de costo ${costo} es 
      ${precio_venta}""")



