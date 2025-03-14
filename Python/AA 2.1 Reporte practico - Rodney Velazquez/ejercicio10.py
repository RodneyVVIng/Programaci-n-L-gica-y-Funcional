# Inicialización de los contadores de puntos para cada rama
redes = 0
bases_de_datos = 0
desarrollo_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_proyectos = 0

# Imprimir el título del programa
print('=========')
print('Sombrero Seleccionador de Ramas de Sistemas Computacionales')
print('=========')

# Pregunta 1
print('\nP1) ¿Qué te interesa más?')
print('  1) Configurar y mantener redes de computadoras')
print('  2) Diseñar y gestionar bases de datos')
print('  3) Desarrollar aplicaciones y software')
print('  4) Programar y trabajar con hardware')
print('  5) Crear modelos y animaciones en 3D')
print('  6) Planificar y gestionar proyectos de software')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 2
print('\nP2) ¿Qué tipo de proyectos te gustaría liderar?')
print('  1) Implementación de infraestructura de red')
print('  2) Optimización de bases de datos')
print('  3) Desarrollo de aplicaciones móviles')
print('  4) Diseño de circuitos electrónicos')
print('  5) Creación de animaciones para videojuegos')
print('  6) Coordinación de equipos de desarrollo')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 3
print('\nP3) ¿Qué habilidades te gustaría desarrollar?')
print('  1) Configuración de routers y switches')
print('  2) Diseño de esquemas de bases de datos')
print('  3) Programación en lenguajes como Python o Java')
print('  4) Trabajar con microcontroladores y sensores')
print('  5) Modelado y texturizado en 3D')
print('  6) Gestión de tiempos y recursos en proyectos')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 4
print('\nP4) ¿En qué área te ves trabajando en el futuro?')
print('  1) Administración de redes y seguridad')
print('  2) Análisis y gestión de datos')
print('  3) Desarrollo de software empresarial')
print('  4) Diseño de hardware y sistemas embebidos')
print('  5) Animación y diseño gráfico')
print('  6) Dirección de proyectos tecnológicos')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Pregunta 5
print('\nP5) ¿Qué tipo de problemas te gustaría resolver?')
print('  1) Problemas de conectividad y comunicación')
print('  2) Problemas de almacenamiento y recuperación de datos')
print('  3) Problemas de automatización y eficiencia')
print('  4) Problemas de integración de hardware y software')
print('  5) Problemas de diseño y visualización')
print('  6) Problemas de planificación y ejecución de proyectos')
respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bases_de_datos += 1
elif respuesta == 3:
    desarrollo_software += 1
elif respuesta == 4:
    programacion_hardware += 1
elif respuesta == 5:
    modelado_3d += 1
elif respuesta == 6:
    gestion_proyectos += 1
else:
    print('Respuesta incorrecta.')

# Imprimir los puntos acumulados para cada rama
print("\nResultados:")
print("Redes: ", redes)
print("Bases de Datos: ", bases_de_datos)
print("Desarrollo de Software: ", desarrollo_software)
print("Programación Hardware: ", programacion_hardware)
print("Modelado 3D: ", modelado_3d)
print("Gestión de Proyectos de Software: ", gestion_proyectos)

# Determinar y anunciar la rama con más puntos
puntos = {
    "Redes": redes,
    "Bases de Datos": bases_de_datos,
    "Desarrollo de Software": desarrollo_software,
    "Programación Hardware": programacion_hardware,
    "Modelado 3D": modelado_3d,
    "Gestión de Proyectos de Software": gestion_proyectos
}

rama_seleccionada = max(puntos, key=puntos.get)
print(f'\n¡La rama más recomendada para ti es: {rama_seleccionada}!')