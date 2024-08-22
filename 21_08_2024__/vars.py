"""
pizza = {"masa":"Tradicional", "salsa":"salsa tomate","ingredientes":["queso"]}
print(pizza["salsa"] )
pizza["salsa"] = "pesto"
print(pizza)
pizza["ingredientes"].append("champiñones")
pizza["ingredientes"].append("choclo")
print(pizza)
if "choclo" in pizza["ingredientes"]:
    print("ok")
from tiempo import tiempo_pizza
#pizza["ingredientes"].pop(pizza["ingredientes"].index("queso"))
print(pizza, tiempo_pizza(pizza))
"""
pizza = {"masa":"Tradicional", "salsa":"salsa tomate","ingredientes":["queso"]}

masas = ["Tradicional","Fina","Borde Queso"]
salsas = ["tomate","alfredo", "barbecue", "pesto"]
ingredientes = ["tomate","champiñones","aceituna","cebolla",
                "pollo","carne","tocino","queso"]