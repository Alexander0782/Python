#Alexander Uribe 21/04

def obtener_articulo(numero):
    if numero == 1:
        return "Hambrurguesa con queso"
    elif numero == 2:
        return "Papas fritas"
    elif numero == 3:
        return "Refresco"
    elif numero == 4:
        return "Helado"
    elif numero == 5:
        return "Nuggets"
    else:
        return "Articulo no encontrado"

print(obtener_articulo(int(input("Ingrese el numero del articulo (1-5): "))))
