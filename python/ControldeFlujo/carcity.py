#Alexander Uribe 3/04/2025

altura = int(input("¿Cual es tu altura? (cm)"))

creditos = int(input("¿Cuantos creditos tienes?"))

if altura >= 137 and creditos >= 10:
    print("Disfruta tu viaje")
elif altura < 137 and creditos >= 10:
    print("No tienes la altura necesaria (enano xddddd)")
elif altura >= 137 and creditos < 10:
    print("Te faltan creditos (pobreeeee)")
else:
    print("No cumples con ningun requisito")