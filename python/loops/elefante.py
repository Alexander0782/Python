#Alexander Uribe 14/04/2025

num_elefante = int(input("¿Cuántos elefantes quieres que canten? : "))

for i in range(1, num_elefante +1):
    if i ==1:
        print(f"{i} elefante se columpiaba sobre la tela de una araña.")
        print("Como veía que no se caía, fue a llamar a otro elefante.")
    else:
        print(f"{i} elefantes se columpiaban sobre la tela de una araña.")
        print("Como veían que no se caían, fueron a llamar a otro elefante.")