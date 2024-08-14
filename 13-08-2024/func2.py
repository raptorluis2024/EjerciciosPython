lista = [x for x in range(10)]

def foo(a):
    print(a)
    
def foobar():
    print(lista)
    
def barFoo(m):
    m = None
    lista = None
    
def FoobarFoo():
    global lista
    lista = None

foo(lista)
foobar()
barFoo(lista)
FoobarFoo()