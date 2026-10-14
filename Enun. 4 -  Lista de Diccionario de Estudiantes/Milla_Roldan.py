# Cada diccionario representa a un estudiante.
# Todos tienen nombre, carrera y promedio.
estudiantes = [
    {"nombre": "Ana", "carrera": "Sistemas", "promedio": 17},
    {"nombre": "Luis", "carrera": "Administración", "promedio": 15},
    {"nombre": "Mía", "carrera": "Contabilidad", "promedio": 19},
    {"nombre": "Juan", "carrera": "Ingeniería Civil", "promedio": 16}
]

# Recorremos los diccionarios de la lista.
for estudiante in estudiantes:
    # Accedemos a los valores usando sus claves.
    print(f"{estudiante['nombre']} | Promedio: {estudiante['promedio']}")

# max() obtiene al estudiante con el promedio más alto.
# lambda indica que debemos comparar el campo "promedio".
mejor = max(estudiantes, key=lambda estudiante: estudiante["promedio"])

# Mostramos los datos del estudiante encontrado.
print(f"\nEstudiante con mayor promedio: {mejor['nombre']}")
print("Promedio:", mejor["promedio"])
