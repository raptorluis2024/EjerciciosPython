""""
Crear un algoritmo que permita ingresar los siguientes datos:
    cantidad de productos
    precio unitario
    departamento (1. Linea blanca, 2.Aseo y Limpieza 3.Refrigeración)
Si la cantidad de productos es mayor a 10 y corresponde al departamento de aseo y limpieza,
el total a pagar tiene un descuento del 8%

Cuando el producto es de refrigeración se debe agregar un 1% de recargo por concepto de 
traslado

Los productos de línea blanca están con un 20% de descuento pero el máximo de unidades por persona es 2.

Al finalizar debe mostrar el detalle de los datos ingresados, los descuentos y/o recargos
correspondientes y el total a pagar por el cliente
    
"""
cantidad = int(input("Ingrese cantidad de productos "))
precio_unitario = int(input("Ingrese precio unitario "))
departamento = int(input("Ingrese Depto 1. Linea blanca, 2.Aseo y Limpieza 3.Refrigeración" ))
recargo=0
descuento=0
"""
Si la cantidad de productos es mayor a 10 y corresponde al departamento de aseo y limpieza,
el total a pagar tiene un descuento del 8%
"""
if cantidad > 10 and departamento == 2:
    a_pagar = (precio_unitario * cantidad)*0.92
    descuento = (precio_unitario * cantidad)*0.08
elif departamento == 3:
    a_pagar = (precio_unitario * cantidad)*1.01
    recargo = (precio_unitario * cantidad)*0.01
elif departamento == 1 and cantidad <= 2:
    a_pagar = (precio_unitario * cantidad)*0.8
    descuento = (precio_unitario * cantidad)*0.2
elif departamento == 1 and cantidad > 2:
    cantidad=0
    a_pagar = 0
else:
    a_pagar = (precio_unitario * cantidad)
print(f"""Compró {cantidad} de productos en el depto {departamento} y el total a pagar es
      {a_pagar:.0f} el decuento es {descuento} y/o recargo es {recargo}
      """)

