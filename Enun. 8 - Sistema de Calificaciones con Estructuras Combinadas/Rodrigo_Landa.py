# Lista de estudiantes.
nombres = ["Ana", "Luis", "Mía", "Juan"]

# Cada materia tiene una lista de notas.
# La posición de cada nota corresponde a la posición del estudiante.
notas = {
    "Matemática": [18, 14, 19, 16],
    "Programación": [17, 16, 20, 15],
    "Comunicación": [16, 15, 18, 17]
}


# Calcula el promedio de las notas de cada materia.
def calcular_promedios_por_materia(notas):
    # Guardaremos un promedio por materia.
    promedios = {}

    # items() permite obtener la materia y su lista de notas.
    for materia, calificaciones in notas.items():
        # Sumamos las notas y dividimos entre su cantidad.
        promedios[materia] = sum(calificaciones) / len(calificaciones)

    return promedios


# Encuentra a los estudiantes con la mejor nota de cada materia.
def mejores_por_materia(nombres, notas):
    mejores = {}

    for materia, calificaciones in notas.items():
        # Obtenemos la nota más alta de la materia.
        nota_maxima = max(calificaciones)

        # Guardaremos todos los nombres que tengan esa nota.
        ganadores = []

        for i in range(len(nombres)):
            # La nota y el nombre se relacionan por el índice i.
            if calificaciones[i] == nota_maxima:
                ganadores.append(nombres[i])

        # Guardamos los ganadores y la nota alcanzada.
        mejores[materia] = {
            "estudiantes": ganadores,
            "nota": nota_maxima
        }

    return mejores


# Genera el ranking según el promedio general de cada estudiante.
def generar_reporte(nombres, notas):
    reporte = []

    # Recorremos cada estudiante por su posición.
    for i in range(len(nombres)):
        total = 0

        # values() obtiene las listas de notas de todas las materias.
        for calificaciones in notas.values():
            # Sumamos la nota de este estudiante en cada materia.
            total += calificaciones[i]

        # len(notas) indica cuántas materias hay.
        promedio_general = total / len(notas)

        # Guardamos el nombre y su promedio general.
        reporte.append({
            "nombre": nombres[i],
            "promedio": promedio_general
        })

    # Ordenamos de mayor a menor promedio.
    reporte.sort(key=lambda estudiante: estudiante["promedio"], reverse=True)

    return reporte


print("PROMEDIOS POR MATERIA")

# Ejecutamos la función que calcula los promedios.
promedios = calcular_promedios_por_materia(notas)

# Mostramos cada materia con su promedio.
for materia, promedio in promedios.items():
    print(f"{materia}: {promedio:.2f}")


print("\nMEJORES ESTUDIANTES POR MATERIA")

# Ejecutamos la función que encuentra las mejores notas.
mejores = mejores_por_materia(nombres, notas)

for materia, resultado in mejores.items():
    # join() une los nombres con una coma si hay empate.
    estudiantes = ", ".join(resultado["estudiantes"])

    print(f"{materia}: {estudiantes} | Nota: {resultado['nota']}")


print("\nREPORTE POR PROMEDIO GENERAL")

# Obtenemos el ranking de estudiantes.
reporte = generar_reporte(nombres, notas)

for i in range(len(reporte)):
    estudiante = reporte[i]

    # Mostramos la posición, el nombre y el promedio.
    print(f"{i + 1}° {estudiante['nombre']} | Promedio: {estudiante['promedio']:.2f}")
