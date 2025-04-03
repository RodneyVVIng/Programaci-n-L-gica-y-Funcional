jugadores = [
    {"nombre": "Brandon", "edad":22},
    {"nombre": "Alan", "edad":23},
    {"nombre": "Oso", "edad":24},
    {"nombre": "Kafai", "edad":25}
]
#usar map
nombres_jugadores = list(map(lambda jugador: ["nombre"], jugadores))
print(nombres_jugadores)