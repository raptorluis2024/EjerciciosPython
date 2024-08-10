import sys
if len(sys.argv) == 1:
       sol = 0.0046
       peso_ar = 0.093
       dolar = 0.00013
       pesos = 10000
else:
       sol = float(sys.argv[1])
       peso_ar = float(sys.argv[2])
       dolar = float(sys.argv[3])
       pesos = int(sys.argv[4])

dic = {"sol":sol,
       "peso_ar":peso_ar,
       "dolar":dolar
       }

print(dic)
print(f"""Los {pesos} pesos equivalen a : 
    {pesos*dic["sol"]} soles
    {pesos*dic["peso_ar"]} Pesos Argentinos
    {pesos*dic["dolar"]} Dólares""")