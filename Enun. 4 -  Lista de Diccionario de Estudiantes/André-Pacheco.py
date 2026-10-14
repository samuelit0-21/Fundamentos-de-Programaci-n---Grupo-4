estudiantes = [
    {"nombre": "Ana", "carrera": "Sistemas", "promedio": 16.5},
    {"nombre": "Carlos", "carrera": "Industrial", "promedio": 18.2},
    {"nombre": "Beatriz", "carrera": "Sistemas", "promedio": 14.8},
    {"nombre": "David", "carrera": "Civil", "promedio": 17.0}
]

print("=== LISTA DE ESTUDIANTES ===")
for est in estudiantes:
    print(f"Nombre: {est['nombre']:<10} | Promedio: {est['promedio']}")

mejor_estudiante = max(estudiantes, key=lambda x: x["promedio"])
print("\nEstudiante con el promedio más alto:")
print(f"-> {mejor_estudiante['nombre']} con promedio de {mejor_estudiante['promedio']}")
