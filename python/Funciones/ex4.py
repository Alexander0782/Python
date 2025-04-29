#Alexander Uribe 28/04

#Objetivo: Acceder a un valor en un diccionario  sin que se rompa el programa si la clave no existe

def buscar_cantante():
    cantante={
        "Nombre":"Luis Miguel",
        "Pais":"Puerto rico"
    }
    try:
        clave = input("¿Que quieres saber?? (Nombre o Pais): ")
        print("Resultado: ",cantante[clave])
    except KeyError:
        print("Esta clabe no existe")

buscar_cantante() 