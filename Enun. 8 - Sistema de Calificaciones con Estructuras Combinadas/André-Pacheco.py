alumnos = ["Juan", "Maria", "Carlos"]

materias_notas = {
    "Matemáticas": [15, 18, 12],
    "Programación": [19, 16, 14],
    "Física": [14, 15, 17]
}

def promedio_materia(materia):
    notas = materias_notas[materia]
    return sum(notas) / len(notas)

def mejor_estudiante_materia(materia):
    notas = materias_notas[materia]
    max_nota = max(notas)
    idx = notas.index(max_nota)
    return alumnos[idx], max_nota

promedios_alumnos = []
for i, alumno in enumerate(alumnos):
    notas_alumno = [materias_notas[mat][i] for mat in materias_notas]
    prom = sum(notas_alumno) / len(notas_alumno)
    promedios_alumnos.append({"nombre": alumno, "promedio": prom})

promedios_alumnos.sort(key=lambda x: x["promedio"], reverse=True)

print("=== REPORTES DE MATERIAS ===")
for mat in materias_notas:
    prom = promedio_materia(mat)
    mejor, nota = mejor_estudiante_materia(mat)
    print(f"Materia: {mat:<12} | Promedio: {prom:.2f} | Mejor Alumno: {mejor} ({nota})")

print("\n=== RANKING GENERAL DE ALUMNOS ===")
for pos, est in enumerate(promedios_alumnos, 1):
    print(f"{pos}°. {est['nombre']:<10} - Promedio General: {est['promedio']:.2f}")
