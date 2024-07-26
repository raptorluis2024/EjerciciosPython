"""
logica proposicional

"""
# and or not
a=True
b=False
c=True
print(a and b or c)

a=True
b=False
c=False
print(a and b or c) # True and False or False


print(True or False or not False)
print(True and False or not False)
print(10%2)

x = int(input("ingrese un numero "))

if x%2 == 0 and x%3 == 0:
    print("ok")
else:
    print("no cumple")
        