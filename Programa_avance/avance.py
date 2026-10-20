# Mesa de Partes Digital

# Expedientes de ejemplo
expedientes = [
    {
        "codigo": "EXP001",
        "nombre": "Juan Perez",
        "dni": "12345678",
        "asunto": "Solicitud de informacion"
    },
    {
        "codigo": "EXP002",
        "nombre": "Maria Lopez",
        "dni": "87654321",
        "asunto": "Solicitud de licencia"
    },
    {
        "codigo": "EXP003",
        "nombre": "Ana Torres",
        "dni": "45612378",
        "asunto": "Reclamo administrativo"
    }
]
# 1. Registrar un expediente
def registrar_expediente():
    print("\n--- REGISTRAR EXPEDIENTE ---")

    codigo = input("Ingrese el codigo: ").strip().upper()

    # Verificamos que el codigo no se repita
    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("Error: el codigo ya existe.")
            return

    nombre = input("Ingrese el nombre del ciudadano: ").strip()
    dni = input("Ingrese el DNI: ").strip()
    asunto = input("Ingrese el asunto: ").strip()

    # Validamos los datos
    if codigo == "" or nombre == "" or dni == "" or asunto == "":
        print("Error: todos los campos son obligatorios.")
        return

    if len(dni) != 8 or not dni.isdigit():
        print("Error: el DNI debe tener 8 numeros.")
        return

    # Creamos el expediente
    nuevo_expediente = {
        "codigo": codigo,
        "nombre": nombre,
        "dni": dni,
        "asunto": asunto
    }

    expedientes.append(nuevo_expediente)

    print("Expediente registrado correctamente.")
