pizza = {"masa":"Tradicional", "salsa":"salsa tomate","ingredientes":["queso"]}
print(pizza["salsa"] )
pizza["salsa"] = "pesto"
print(pizza)
pizza["ingredientes"].append("champiñones")
print(pizza)
if "choclo" in pizza["ingredientes"]:
    print("ok")
    
pizza["ingredientes"].pop(pizza["ingredientes"].index("queso"))
print(pizza)