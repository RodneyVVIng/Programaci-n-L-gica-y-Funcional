asignaturas_viii = ['Programacion logica y funcional']
"b = asignaturas_viii + ['web']"

"print(asignaturas_viii, b)"

def agregar_asignatura (lista, asignatura):
    return lista + [asignatura]

xd = input('ingresa nueva asignatura')

print(agregar_asignatura(asignaturas_viii, xd))