def agregar_asignatura(lista):
    asig_nue = input("ingresa nueva asignatura o 'no' para salir: ")
    if asig_nue == "no":
        return lista
    return agregar_asignatura(lista + [asig_nue])

asignaturas = ["Graficacion", "Automatas", "Investigacion"]

print(agregar_asignatura(asignaturas))