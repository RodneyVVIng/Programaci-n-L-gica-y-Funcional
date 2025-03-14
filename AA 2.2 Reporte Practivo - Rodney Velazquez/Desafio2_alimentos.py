
def preparar_pizza():
    return "🍕"
def preparar_hamburguesa():
    return "🍔"
def preparar_hotdog():
    return"🌭"

def ordenar_alimento(prepararA, nu_porciones):
    porciones_A = [prepararA() for _ in range(nu_porciones)]
    bonus = calcular_bonus(nu_porciones)
    return porciones_A, bonus

def calcular_bonus(num):
    if(num > 2):
        return "coca gratis"
    else:
        return ""

print(ordenar_alimento(preparar_pizza, 2))
print(ordenar_alimento(preparar_hamburguesa, 5))
print(ordenar_alimento(preparar_hotdog, 2))