jugadores = [
    {"nombre": "Brandon", "edad":22},
    {"nombre": "Alan", "edad":23},
    {"nombre": "Oso", "edad":24},
    {"nombre": "Kafai", "edad":25}
]

jugadores_mayores = list(filter(lambda jugador: jugador["edad"] > 23, jugadores))

print(jugadores_mayores)