def factorial( n=1):
    if n == 0 or n == 1:
        return 1
    fact = 1
    while True:
        fact *= n
        n -= 1
        if n == 1:
            break
    return fact

def factorial_1(n):
    fact=1
    if n == 0 or n == 1:
        return 1
    for x in range(1,n+1):
        fact *= x
    return fact

def productoria(lista):
    prod=1
    for x in lista:
        prod *= x
    return prod

def calcular(fact_1=1, prod_1=[1], fact_2=1):
    print(f"El factorial de {fact_1} es : {factorial(fact_1) }")
    print(f"La productoria de {prod_1} es {productoria(prod_1)}")
    print(f"El factorial de {fact_2} es {factorial(fact_2)}")

def calcular1( **kwargs ):
    for k,v in kwargs.items():
        if "fact" in k:
            print(f"El factorial de {v} es : {factorial(v) }")
        else:
            print(f"La productoria de {v} es {productoria(v)}")

calcular(fact_1=5, prod_1=[4,6,7,4,3], fact_2 = 6)
calcular1(fact_1=5, prod_1=[4,6,7,4,3], fact_2 = 6, fact_3=9)
        