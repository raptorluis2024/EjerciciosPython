responde = input("Responde a estimulos s/n ")
if responde.upper() == "S":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
else:
    print("Abrir la vía aérea")
    respira = input("respira s/n ")
    if respira.upper() == "S":
        print("Permitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar la ambulancia")
        ambulancia = "N"
        while ambulancia == "N":
            signos = input("Tiene signos de vida s/n ")
            if signos.upper() == "S":
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
            ambulancia = input("Llegó la ambulancia s/n ").upper()
print("Ojalá se salve")