import csv
import os

def crear_csv_ejemplo(archivo="estudiantes.csv"):
    """Crea un archivo CSV de ejemplo si no existe."""
    if not os.path.exists(archivo):
        with open(archivo, mode="w", newline="", encoding="utf-8") as file:
            escritor = csv.writer(file)
            # Encabezados
            escritor.writerow(["nombre", "matematica", "comunicacion", "ciencia"])
            # Datos de ejemplo
            escritor.writerow(["Ana", 15, 18, 12])
            escritor.writerow(["Carlos", 10, 11, 9])
            escritor.writerow(["Lucía", 16, 14, 17])
            escritor.writerow(["Pedro", 8, 9, 7])
            escritor.writerow(["María", 14, 15, 13])
        print(f"Archivo '{archivo}' creado correctamente con datos de ejemplo.\n")

def analizar_notas(archivo="estudiantes.csv"):
    """
    Lee un archivo CSV con notas de estudiantes, calcula el promedio por alumno,
    identifica al estudiante con mayor promedio y cuenta cuántos aprobaron (promedio ≥ 13).
    """
    # Crear el archivo de ejemplo si no existe
    crear_csv_ejemplo(archivo)
    
    estudiantes = []
    
    # Abrir el archivo CSV en modo lectura
    with open(archivo, mode="r", encoding="utf-8") as file:
        lector = csv.DictReader(file)
        
        for fila in lector:
            nombre = fila["nombre"]
            
            # Extraer y convertir las notas a float
            notas = [float(valor) for clave, valor in fila.items() if clave != "nombre"]
            
            # Calcular promedio
            promedio = sum(notas) / len(notas)
            
            estudiantes.append({"nombre": nombre, "promedio": promedio})
    
    if not estudiantes:
        print("No se encontraron estudiantes en el archivo.")
        return
    
    # Obtener el estudiante con mayor promedio
    top_alumno = max(estudiantes, key=lambda x: x["promedio"])
    
    # Contar aprobados (promedio ≥ 13)
    aprobados = sum(1 for est in estudiantes if est["promedio"] >= 13)
    
    # Mostrar resultados
    print("=== Resultados del Análisis ===")
    print(f"Total de estudiantes: {len(estudiantes)}")
    print(f"Estudiantes que aprobaron (prom ≥ 13): {aprobados}")
    print(f"Top alumno: {top_alumno['nombre']} con promedio {top_alumno['promedio']:.2f}")

# Ejecutar el análisis
analizar_notas()