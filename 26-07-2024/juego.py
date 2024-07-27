import sys
import random
jugada = sys.argv[1]
lista = ["papel", "tijera","piedra"]
print(jugada, random.choice(lista))