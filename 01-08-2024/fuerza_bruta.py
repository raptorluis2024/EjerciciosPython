from string import ascii_lowercase
import getpass
palabra = getpass.getpass("Ingrese la contraseña ")
abc = ascii_lowercase
veces = 0
for letra in palabra:
    for caracter in abc:
        veces += 1
        if letra == caracter:
            break
print(f"intentos {veces}")
