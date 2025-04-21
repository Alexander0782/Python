#Alexander Uribe 16/04/2025

# Alcance local

def suma(a, b):
    resultado = a + b
    return resultado
print(suma(5, 10))

#alcance global

respuesta = 0
def sumar(x,y):
    respuesta = x + y
    return respuesta
print(sumar(5, 10))