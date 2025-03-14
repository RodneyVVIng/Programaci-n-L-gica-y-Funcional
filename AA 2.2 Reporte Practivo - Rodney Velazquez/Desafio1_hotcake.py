def preparar_HK():
    return "🥞"

def ordenar_NHK(nu_piezas):
    piezas_hotcakes = [preparar_HK() for _ in range(nu_piezas) ]
    return piezas_hotcakes

cafe_grupoA = ordenar_NHK(int(input('Ingresa tu orden bitch ')))
print(cafe_grupoA)