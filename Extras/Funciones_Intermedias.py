#Alexander Uribe 12/05
# #tareas de python

matriz = [ [10, 15, 20], [6, 7, 14] ]
cantantes = [
    {"nombre": "Enrique Martin Morales", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Monterrey"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 9.9355431, "longitud": -84.9399704}
]

def iterarDiccionario(lista):
    for i in lista:
        for j in i:
            print(f"{j}: {i[j]}")
    return

iterarDiccionario(cantantes)


print("      "
    "espacioo" 
    "        ")

def iterarDiccionario2(llave,lista):
    for i in lista:
        if llave in i:
            print(f"{llave}: {i[llave]}")
        else:
            print(f"{llave} no encontrado en el diccionario")
    return


iterarDiccionario2("nombre",cantantes)