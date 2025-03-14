
def preparar_cafe():
    return "cafe"

def ordenar_cafe(nu_tazasC):
    tazas_cafe = [preparar_cafe() for _ in range(nu_tazasC)]
    return tazas_cafe

#cadena = ["Hola"+"que hace" for _ in range (4)]

cafe_grupoA = ordenar_cafe(int(input('Ingresa tu orden bitch ')))
print(cafe_grupoA)