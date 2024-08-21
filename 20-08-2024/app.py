""" 
import random
lista = [random.randrange(1,20) for x in range(10)]

import random as r
lista = [r.randrange(1,20) for x in range(10)]

from random import randrange, random, choice
lista = [randrange(1,20) for x in range(10)]

"""
from var import lista
import mod1
import mod2
from mod1 import promedio as prom1
from mod2 import promedio as prom_pares
from utils.mod3 import listar

print(lista, mod1.promedio(lista))
print(prom1(lista))
print(lista, prom_pares(lista))
print(lista, mod2.promedio(lista),mod2.sqrt_prom(lista))
listar(lista)