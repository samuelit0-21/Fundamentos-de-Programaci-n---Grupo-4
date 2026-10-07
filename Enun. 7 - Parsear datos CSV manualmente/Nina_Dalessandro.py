lineas_csv = [
    "Juan Perez, 85, Lima",
    "Maria Lopez, 92, Arequipa",
    "Carlos Ruiz, 78, Trujillo"
]

print("== REPORTE DE ESTUDIANTES ==")
for linea in lineas_csv:
    partes = linea.split(",")
    nombre = partes[0].strip()
    nota = partes[1].strip()
    ciudad = partes[2].strip()
    print(f"Estudiante: {nombre:<15} | Nota: {nota:<3} | Ciudad: {ciudad}")
