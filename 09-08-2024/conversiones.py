import sys
dic = {"sol":float(sys.argv[1]),
       "peso_ar":float(sys.argv[2]),
       "dolar": float(sys.argv[3])
       }
pesos = int(sys.argv[4])
print(dic)
print(f"""Los {pesos} pesos equivalen a : 
    {pesos*dic["sol"]} soles
    {pesos*dic["peso_ar"]} Pesos Argentinos
    {pesos*dic["dolar"]} Dólares""")