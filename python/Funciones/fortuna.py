#Alexander Uribe 14/04

import random
def fortuna():
    "nose"

opciones = ["No persigas la felicidad, creala",
            "todas las cosas son dificiles antes de ser facil",
            "El pajaro madrugador atrapa el gusano, pero el segundo raton se ll",
            "Alguien en tu vida necesita una carta de tu parte",
            "No lo pienses.¡Actua!",
            "Tu corazon se acelarara",
            "La fortuna que buscas esta en otra galleta",
            "¡Ayuda!¡Estoy preso en una panaderia china!",]

def fortuna():
    fortuna = random.randint(0, len(opciones)-1)
    print(opciones[fortuna])

fortuna()