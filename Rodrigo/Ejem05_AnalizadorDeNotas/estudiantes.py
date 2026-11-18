# Importamos el modulo csv
import csv

# Creamos una lista para guardar los estudiantes
estudiantes = []

# Abrimos el archivo CSV
with open("estudiantes.csv", "r", encoding="utf-8") as archivo:

    # Leemos los datos del archivo
    lector = csv.DictReader(archivo)

    # Recorremos cada estudiante
    for fila in lector:

        # Calculamos el promedio
        promedio = (float(fila["nota1"]) +
                    float(fila["nota2"]) +
                    float(fila["nota3"])) / 3

        # Guardamos el nombre y promedio
        estudiantes.append({
            "nombre": fila["nombre"],
            "promedio": promedio
        })


# Mostramos los promedios
for alumno in estudiantes:
    print(alumno["nombre"], alumno["promedio"])


# Buscamos al estudiante con mejor promedio
mejor = max(estudiantes, key=lambda x: x["promedio"])

print("Mejor alumno:", mejor["nombre"])
print("Mejor promedio:", mejor["promedio"])


# Contamos los estudiantes aprobados
aprobados = sum(1 for alumno in estudiantes
                if alumno["promedio"] >= 13)

print("Cantidad de aprobados:", aprobados)
