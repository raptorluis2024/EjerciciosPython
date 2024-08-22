#ingredientes=["Tomate", "Champiñones", "Choclo"]
#print(f"Ingredientes {ingredientes}")
#from utils import fx
import os
import sys

if sys.platform == "win32":
    os.system("cls")
    
from menu import menu_principal,menu_masas,menu_salsas,menu_ingredientes
from vars import pizza,ingredientes
from tiempo import aceptarPedido
import utils as u

opc=0
print("Pizza JAT")
while True:
    
    opc = menu_principal()
    if opc == 1:
        base = menu_masas()
        u.cambiarmasa(pizza,base)
    elif opc == 2:
        salsa = menu_salsas()
        u.cambiarsalsa(pizza,salsa)
    elif opc == 3:
        ingrediente = ingredientes[menu_ingredientes()]
        print("Ingrediente agregado") if u.agregar_ingrediente(pizza,ingrediente) else print("Ingrediente existe en la pizza")
    elif opc == 4:
        ingrediente = ingredientes[menu_ingredientes()]
        print("Ingrediente eliminado") if u.eliminar_ingrediente(pizza,ingrediente) else print("Ingrediente NO existe en la pizza")
    elif opc == 5:
        print(pizza)
    elif opc == 6:
        aceptarPedido(pizza)
    elif opc == 7:
        break
    else:
        print("Opción No válida")
