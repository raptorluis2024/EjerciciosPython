a=200
def Foo(x):
    #a=110
    global a
    a=110
    return x+a
    
print(a)    
Foo(1000)
print(a)