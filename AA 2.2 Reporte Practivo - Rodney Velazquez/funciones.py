'''#EJEMPLO CALLBACK
def operar(n1, n2 ,funcion):
    return funcion(n1, n2)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

resultado = operar (5, 3, suma)
print(resultado)
'''
'''#Ejemplo funcion primera clase

def saludo():
    return"Hola gay"

mi_variable = saludo()
print(mi_variable)

def saludo2 ():
    return "Hola de nuevo gay"

mi_variable2 = saludo2
print(saludo2())'''

#EJEMPLO FUNCION DE RORDEN SUPERIOR

'''def elegir_operacion(operacion):
    def multiplicar(x):
        return x * 2
    def dividir(x):
        return x / 2
    if operacion == "multiplicar":
        return multiplicar
    else:
        return dividir
doble = elegir_operacion("multiplicar")
print(doble(10))
divide2 = elegir_operacion("dividir")
print(divide2(10))'''

#EJEMPLO UNA FUNCION ANONIMA LAMBDA

'''doble = lambda x: x * 2
print(doble(5))

numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

alumnos = ['Memo', 'Wilgay', 'Cobos', 'HonyTzis', 'SantosAlv']
saludar_alumnos = list(map(lambda nombre: 'Hola pinche ' + nombre, alumnos))
#print(saludar_alumnos)'''

#Sin Lambda

'''def saludar(nombre):
    return 'Hola maldito ' + nombre
#Usamos map con la funcion saludar
lista_saludos = list(map(saludar, alumnos))
print(lista_saludos)'''

def preparar_cafe():
    return "cafe"