mes = ["Octubre","Noviembre","Diciembre"]
ventas = [65000, 68000,72000]
dic = {k:v for k,v in zip(mes,ventas) }
print(dic)
dic1 = {k:v*2.2 for k,v in dic }
dic2 ={k:v*0.8 for k,v in zip(mes,ventas) }
print(dic2)