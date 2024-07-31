"""
Para poder ingresar notas debe primero ingresar una password, al
tercer intento el usuario es bloqueado y debe emitir un mensaje
indicando que superó los tres intentos.
clave = "VamosConTodo"

EL programa debe permitir el ingreso de 5 notas validadas en el rango
Se debe imprimir el promedio una vez que finalice el programa

v2.0 Indicar cuál fue la menor y la mayor nota ingresada durante el proceso

"""

import getpass
error=0
while True:
    claveusuario = getpass.getpass()
    clave = "VamosConTodo"
    if claveusuario == clave:
        suma=0
        for x in range(5):
            while True:
                nota = float(input("Ingrese una nota "))
                if nota >= 1 and nota <= 7:
                    print("Nota valida")
                    suma += nota  # suma = suma + nota
                    break
                else:
                    print("nota inválida")
                    continue
        print(f"El promedio es {suma/5:.2f}")
        siono = input("Quiere seguir s/n").upper()
        if siono != "S":
            break
        else:
            error=0
    else:
        error += 1
        if error > 2:
            print("Te piteaste mas de 3 intentos")
            break
        else:
            print("Clave incorrecta")
        
        
   