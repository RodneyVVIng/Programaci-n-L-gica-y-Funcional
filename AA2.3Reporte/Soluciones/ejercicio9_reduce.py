from functools import reduce

jugadores = [
    {"nombre": "Brandon", "edad":22},
    {"nombre": "Alan", "edad":23},
    {"nombre": "Oso", "edad":24},
    {"nombre": "Kafai", "edad":25}
]

suma_edad = reduce(lambda acumulador, jugador: acumulador+jugador ["edad"], jugadores,0 )
print(suma_edad)