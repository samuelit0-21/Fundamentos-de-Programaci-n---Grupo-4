# MESA DE PARTES DIGITAL

from datetime import datetime

# Importamos la lista de expedientes
from datos import expedientes
from almacenamiento import guardar_expedientes


def registrar_expediente():
    """Permite registrar un nuevo expediente."""

    print("\n--- REGISTRO DE EXPEDIENTE ---")

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

    # Establecer el formato de fecha DD/MM/AAAA
    FORMATO_FECHA = "%d/%m/%Y"
    fecha_ingreso_formateada = datetime.now().strftime(FORMATO_FECHA)

# Crear el nuevo expediente con todos sus datos incluida la fecha
    nuevo_expediente = {
        "codigo": codigo,
        "nombre": nombre,
        "dni": dni,
        "asunto": asunto,
        "estado": "Pendiente",
        "fecha_ingreso": fecha_ingreso_formateada,
    }

    # Almacenar la fecha junto con los demás datos del expediente
    expedientes.append(nuevo_expediente)
    guardar_expedientes(expedientes)

    print("Expediente y fecha de ingreso almacenados correctamente.")
    print(f"Fecha de ingreso registrada: {nuevo_expediente['fecha_ingreso']}")
    print("Estado inicial: Pendiente")
