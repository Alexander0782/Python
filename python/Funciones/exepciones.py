#alexander uribe 28/04

#Objetivo: Pedir un numero al usuario y evitar errores si escribe letras

def pedir_numero():
    try:
        numero = int(input("Escribe un numero entero: "))
        print("¡Gracias! Tu numero es: ", numero)
    except ValueError:
        print("ese no es un numero esperado, intentelo de nuevo")
        pedir_numero()

pedir_numero()