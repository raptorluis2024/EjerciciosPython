def fun(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,v)

fun(valor=1, edad=19, apellido="parra", nacionalidad="CH")
fun(valor=12, edad=29, apellido="gómez", lista=[1,2,3,4,4])