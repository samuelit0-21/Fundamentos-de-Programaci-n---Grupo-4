# MESA DE PARTES DIGITAL

# Importamos la lista de expedientes
from datos import expedientes


def registrar_expediente():
    """Permite registrar un nuevo expediente."""

    print("\n--- REGISTRO DE EXPEDIENTE ---")

    codigo = input("Ingrese el codigo del expediente: ").strip().upper()
    nombre = input("Ingrese el nombre del solicitante: ").strip()
    dni = input("Ingrese el DNI: ").strip()
    asunto = input("Ingrese el asunto: ").strip()

    # Validar que los campos no esten vacios
    if not codigo or not nombre or not dni or not asunto:
        print("Todos los campos son obligatorios.")
        return

    # Validar que el DNI tenga 8 digitos numericos
    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe tener exactamente 8 digitos.")
        return

    # Verificar que el codigo no exista
    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("El codigo ya se encuentra registrado.")
            return

    # Crear el nuevo expediente
    nuevo_expediente = {
        "codigo": codigo,
        "nombre": nombre,
        "dni": dni,
        "asunto": asunto,
        "estado": "Pendiente"
    }

    # Agregar el nuevo expediente a la lista
    expedientes.append(nuevo_expediente)

    print("Expediente registrado correctamente.")
    print("Estado inicial: Pendiente")
