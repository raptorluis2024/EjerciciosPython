"""
Crear un algoritmo que permita ingresar por pantalla la nacionalidad de una persona
1 = Chilena
2 = Extranjero
El usuario decide cuántas personas contabilizará.
Al finalizar el programa debe imprimir:
    Cantidad de chilenos
    Cantidad de Extranjeros
    % de Chilenos versus Extranjeros
"""
chilenos = 0
extranjeros =0
sigue = "S"
while sigue == "S":
    nacionalidad = int(input("Nacionalidad 1=CH 2=EX"))
    if nacionalidad == 1: ## contar chileno
        chilenos += 1
    elif nacionalidad == 2: ## contar un extranjero
        extranjeros += 1
    else:
        print("valor no válido")  
    sigue = input("Desea continuar s/n").upper()
print(f"""Chilenos {chilenos}, extranjeros {extranjeros}
       % de chilenos versus extranjeros {chilenos/extranjeros:.2f}
      """,)
