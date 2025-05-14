#Alexander Uribe 12/05
#tareas de python

print("\n ejercicio 1: Basico")
for i in range(101):
    print(f"Numero actual: {i}")

print("\n ejercicio 2: Multiple")
for i in range(2, 500, 2):
    print(i)

print("\n ejercicio 3: Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("Baby")
    elif i % 5 == 0:
        print("Ice Ice")
    else:
        print(i)

print("\n ejercicio 4: Numero gigante")
suma_total = 0
for i in range(1, 500001, 2):
    suma_total += i
print(suma_total)

print("\n ejercicio 5: de 3 em 3")
for i in range(2024, 0, -3):
    print(i)

print("\n ejercicio 6: multiplos")
numero_inicial = 3
numero_final = 100
multiplo = 2
for i in range(numero_inicial, numero_final + 1):
    if i % multiplo == 0:
        print(i)
