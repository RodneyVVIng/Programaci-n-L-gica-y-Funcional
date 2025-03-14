# Inicialización de los contadores de puntos para cada casa
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

# Imprimir el título del Sombrero Seleccionador
print('=========')
print('El sombrero seleccionador 🟧')
print('=========')

# Pregunta 1
print('P1) ¿Te gusta el amanecer o el atardecer?')
print('  1) Amanecer')
print('  2) Atardecer')
respuesta = int(input('Ingresa respuesta (1-2): '))

if respuesta == 1:
    gryffindor += 1
    ravenclaw += 1
elif respuesta == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 2
print('\nP2) Cuando muera, quiero que la gente me recuerde como:')
print('  1) El bueno o la buena')
print('  2) El valiente o la valiente')
print('  3) El sabio o la sabia')
print('  4) El astuto o la astuta')
respuesta = int(input('Ingresa tu respuesta (1-4): '))

if respuesta == 1:
    hufflepuff += 2
elif respuesta == 2:
    slytherin += 2
elif respuesta == 3:
    ravenclaw += 2
elif respuesta == 4:
    gryffindor += 2
else:
    print('Respuesta incorrecta.')

# Pregunta 3
print('\nP3) ¿Qué tipo de instrumento complace más tu oído?')
print('  1) El violín')
print('  2) La trompeta')
print('  3) El piano')
print('  4) El tambor')
respuesta = int(input('Ingresa tu respuesta (1-4): '))

if respuesta == 1:
    slytherin += 4
elif respuesta == 2:
    hufflepuff += 4
elif respuesta == 3:
    ravenclaw += 4
elif respuesta == 4:
    gryffindor += 4
else:
    print('Respuesta incorrecta.')

# Imprimir los puntos acumulados para cada casa
print("\nResultados:")
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

# Determinar y anunciar la casa a la que el usuario ha sido asignado
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print('\n¡Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print('\n¡Ravenclaw!')
elif hufflepuff >= slytherin:
    print('\n¡Hufflepuff!')
else:
    print('\n¡Slytherin!')