def sumar(*args):
    suma=0
    for x in args:
        if type(x) is int or type(x) is float:
            suma += x
        elif type(x) is list:
            suma += sum(x)
    return suma

print(sumar("A",8,9,[1,2],9,11.1,[1.5,3.0]))