#Alexander Uribe 28/04

#Objetivo: Mostrar un elemento de una lista por su posición, manejando si la posición no existe
def mostrar_elemento():
    frutas = ["Manzana","Platano","Naranja","Palta"]
    try:
        indice = int(input("Elije una posicion (0 a 3): "))
        print("Fruta elejida: ", frutas[indice])
    except IndexError:
        print("esta posicion no existe en la lista, utilice los numeros indicados")
        mostrar_elemento()
    except ValueError:
        print("Valor incorrecto, utilize numeros")
        mostrar_elemento()

mostrar_elemento()
