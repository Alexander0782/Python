#Alexander Uribe

#Objetivo: Repetir hasta que lo hagan bien, podemos usar un bucle junto con un try

def pedir_numero_repetido():
    while True:
        try:
            numero = int(input("Escribe un numero entero: "))
            print("Tu numero es: ", numero)
            break
        except ValueError:
            print("Ese no es un numero, intentelo de nuevo:")

pedir_numero_repetido()