#ingredientes=["Tomate", "Champiñones", "Choclo"]
#print(f"Ingredientes {ingredientes}")
#from utils import fx

from menu import menu_principal,menu_masas,menu_salsas
from vars import pizza,masas,salsas
import utils as u

opc=0
print("Pizza JAT")
while True:
    opc = menu_principal()
    if opc == 7:
        break
    elif opc == 1:
        base = menu_masas()
        #pizza["masa"] = masas[base]
        u.cambiarmasa(pizza,base)
    elif opc == 2:
        salsa = menu_salsas()
        pizza["salsa"] = salsas[salsa]
    elif opc == 5:
        print(pizza)