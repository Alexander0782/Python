#Alexander Uribe 2/04/2025

respuesta = input("Estas cansado) (si/no):").strip().lower()

cansado = respuesta == "si"

if not cansado:
    print("TRABAJAAA")
else:
    print("A descansar noma")