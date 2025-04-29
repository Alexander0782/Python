#Alexander Uribe 28/04

def funcion(a,b,*args,**kwargs):
    print("a =", a)
    print("b =", b)
    for arg in args:
        print("arg =", arg)
    for key, value in kwargs.items():
        print("Kwarg =", key," = ",value)

funcion(1,2, 14,28,21,36,37, x="luis", y="sol", c="Mexico")
