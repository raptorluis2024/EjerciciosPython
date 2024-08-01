pais =["Mexico", "Chile", "Argentina"]
usuarios = [70,50,55]

filtro = {k:v for k,v in zip(pais,usuarios) if v <60}
print(filtro)