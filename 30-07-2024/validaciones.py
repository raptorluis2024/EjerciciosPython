"""
Para poder ingresar notas debe primero ingresar una password, al
tercer intento el usuario es bloqueado y debe emitir un mensaje
indicando que superó los tres intentos.
clave = "VamosConTodo"

EL programa debe permitir el ingreso de 5 notas validadas en el rango
Se debe imprimir el promedio una vez que finalice el programa

v2.0 Indicar cuál fue la menor y la mayor nota ingresada durante el proceso

"""

#import getpass
#a = getpass.getpass()

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