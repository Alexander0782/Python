#Alexander Uribe 16/04

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def potencia(a, b):
    return a ** b

print(suma(int(input(" Suma, Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))))
print(resta(int(input("Resta, Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))))
print(multiplicacion(int(input("Multiplicación, Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))))
print(division(int(input("División, Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))))
print(potencia(int(input("Potencia, Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))))