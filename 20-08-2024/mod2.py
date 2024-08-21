###
import math
import mod1

def promedio(L):
    paso = [x for x in L if x%2==0]
    return round(sum(paso)/len(paso),2),paso 
def sqrt_prom(L):
    return round(math.sqrt(mod1.promedio(L)),2)