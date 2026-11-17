# Importamos el módulo csv para trabajar con archivos CSV
import csv

# Creamos un diccionario vacío para almacenar las notas
notas = {}

# Abrimos el archivo CSV en modo lectura
with open("estudiantes.csv", "r", encoding="utf-8") as archivo:

    # Leemos el archivo utilizando los nombres de las columnas
    lector = csv.DictReader(archivo)

    # Recorremos cada fila del archivo
    for fila in lector:

        # Obtenemos el nombre del alumno
        alumno = fila["alumno"]

        # Convertimos la nota de texto a número decimal
        nota = float(fila["nota"])

        # Verificamos si el alumno todavía no está registrado
        if alumno not in notas:

            # Creamos una lista vacía para sus notas
            notas[alumno] = []

        # Agregamos la nota correspondiente al alumno
        notas[alumno].append(nota)


# Creamos un diccionario para guardar los promedios
promedios = {}

# Recorremos las notas de cada alumno
for alumno, calificaciones in notas.items():

    # Calculamos el promedio de sus calificaciones
    promedio = sum(calificaciones) / len(calificaciones)

    # Guardamos el promedio en el diccionario
    promedios[alumno] = promedio

    # Mostramos el promedio de cada alumno
    print(alumno, "Promedio:", promedio)


# Buscamos al alumno que tiene el promedio más alto
mejor_alumno = max(promedios, key=promedios.get)

# Mostramos el alumno con mejor promedio
print("\nMejor alumno:", mejor_alumno)

# Mostramos su promedio
print("Mejor promedio:", promedios[mejor_alumno])


# Contamos los alumnos que tienen promedio mayor a 13
aprobados = sum(
    1 for promedio in promedios.values() if promedio > 13
)

# Mostramos la cantidad de alumnos aprobados
print("Alumnos aprobados:", aprobados)
