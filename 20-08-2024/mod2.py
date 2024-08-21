###
def promedio(L):
    paso = [x for x in L if x%2==0]
    return round(sum(paso)/len(paso),2),paso 
