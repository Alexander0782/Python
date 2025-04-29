#Alexander Uribe 28/04

def suma(*args):
    s=0
    for arg in args:
        s += arg
    return s
resultado = suma(1,2,3,4)
print(resultado)