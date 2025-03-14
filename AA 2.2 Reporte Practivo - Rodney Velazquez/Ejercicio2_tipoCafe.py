
def preparar_cafeA():
    return "cafe Americano"
def preparar_cafeO():
    return "cafe de Olla"

def ordenar_cafe(preparar, nu_tazasC):
    tazas_cafe = [preparar() for _ in range(nu_tazasC)]
    return tazas_cafe

cafe_grupoA = ordenar_cafe(preparar_cafeA,int(input("Numero de tazas ")))
print(cafe_grupoA)

cafe_grupoB = ordenar_cafe(preparar_cafeO,int(input("Numero de tazas ")))
print(cafe_grupoB)