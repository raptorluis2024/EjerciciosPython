import getpass
a = getpass.getpass()

while True:
    nota = float(input("Ingrese una nota "))
    if nota >= 1 and nota <= 7:
        print("Nota valida")
        break
    else:
        print("nota inválida")
        continue
