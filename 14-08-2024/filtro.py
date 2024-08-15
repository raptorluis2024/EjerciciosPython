import sys
precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

def filtro(umbral, mayormenor=0):
    if mayormenor == 1:
        return [k for k, v in precios.items() if v > umbral ]
    elif mayormenor == 2:
        return [k for k, v in precios.items() if v < umbral ]
    else:
        return "Lo sentimos no es una operación válida"
        
if len(sys.argv) == 2 or len(sys.argv) == 3 and sys.argv[2] == "mayor":
    print(f"Los productos mayores al umbral son {', '.join(filtro(int(sys.argv[1]),1))}")
elif sys.argv[2] == "menor":
    print(f"Los productos menores al umbral son {', '.join(filtro(int(sys.argv[1]),2))}")
else:
    print(filtro(int(sys.argv[1])))


