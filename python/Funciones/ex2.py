#Alexander Uribe

def divisiones():
    try:
        num1 = int(input("Ingresa un numero: "))
        num2 = int(input("Ingresa otro numero: "))
        resultado = num1 / num2
        print("El resultado de la division es: ", resultado)
    except ZeroDivisionError:
        print("esta division no se puede hacer, intenta con otros numeros")
        divisiones()
    except ValueError:
        print("estos no son numeros, intentelo de nuevo")
        divisiones()

divisiones()