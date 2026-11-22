
# MESA DE PARTES DIGITAL

from datetime import datetime
import random

# Importamos la lista de expedientes
from datos import expedientes
from almacenamiento import guardar_expedientes


# Categorías y trámites sugeridos
CATEGORIAS = {
    "1": {
        "nombre": "Tributarios y prediales",
        "tramites": [
            "Consulta de impuesto predial",
            "Consulta de arbitrios",
            "Solicitud de fraccionamiento",
            "Reclamo tributario"
        ]
    },
    "2": {
        "nombre": "Documentación y constancias municipales",
        "tramites": [
            "Solicitud de constancia",
            "Solicitud de copia de documentos",
            "Solicitud de información sobre documentos municipales"
        ]
    },
    "3": {
        "nombre": "Solicitudes administrativas municipales",
        "tramites": [
            "Solicitud dirigida a un área municipal",
            "Presentación de documentos",
            "Solicitud de atención administrativa"
        ]
    },
    "4": {
        "nombre": "Reclamos y consultas",
        "tramites": [
            "Reclamo por servicio municipal",
            "Consulta sobre atención municipal",
            "Reclamo por limpieza pública, parques o mantenimiento"
        ]
    },
    "5": {
        "nombre": "Otros trámites",
        "tramites": [
            "Otro trámite"
        ]
    }
}


def generar_codigo_unico():
    """Genera un código único con formato EXP-AAAA-XXXXXX."""

    anio = datetime.now().year

    while True:
        seis_digitos = str(random.randint(0, 999999)).zfill(6)
        codigo = f"EXP-{anio}-{seis_digitos}"

        # Verificar que el código no exista
        existe = False

        for expediente in expedientes:
            if expediente["codigo"] == codigo:
                existe = True
                break

        if not existe:
            return codigo


def seleccionar_categoria():
    """Muestra las categorías y permite seleccionar un trámite."""

    print("\n--- CATEGORÍAS DE SOLICITUDES ---")

    for numero, categoria in CATEGORIAS.items():
        print(f"{numero}. {categoria['nombre']}")

    while True:
        opcion = input("\nSeleccione una categoría: ").strip()

        if opcion in CATEGORIAS:
            categoria_seleccionada = CATEGORIAS[opcion]
            nombre_categoria = categoria_seleccionada["nombre"]
            tramites = categoria_seleccionada["tramites"]

            print(f"\n--- TRÁMITES: {nombre_categoria} ---")

            for numero, tramite in enumerate(tramites, start=1):
                print(f"{numero}. {tramite}")

            while True:
                opcion_tramite = input(
                    "\nSeleccione un trámite: "
                ).strip()

                if opcion_tramite.isdigit():
                    numero = int(opcion_tramite)

                    if 1 <= numero <= len(tramites):
                        asunto = tramites[numero - 1]

                        if asunto == "Otro trámite":
                            asunto = input(
                                "Describa su solicitud: "
                            ).strip()

                            if not asunto:
                                print("Debe ingresar una descripción.")
                                continue

                        return nombre_categoria, asunto

                print("Seleccione una opción válida.")

        else:
            print("Categoría no válida. Intente nuevamente.")


def registrar_expediente():
    """Permite registrar un nuevo expediente."""

    print("\n--- REGISTRO DE EXPEDIENTE ---")

    nombre = input("Ingrese el nombre del solicitante: ").strip()
    dni = input("Ingrese el DNI: ").strip()

    # Validar que los campos no estén vacíos
    if not nombre or not dni:
        print("Todos los campos son obligatorios.")
        return

    # Validar que el DNI tenga 8 dígitos numéricos
    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe tener exactamente 8 dígitos.")
        return

    # Seleccionar categoría y trámite
    categoria, asunto = seleccionar_categoria()

    # Generar código único
    codigo = generar_codigo_unico()

    # Registrar fecha de ingreso
    fecha_ingreso_formateada = datetime.now().strftime("%d/%m/%Y")

    # Crear el nuevo expediente
    nuevo_expediente = {
        "codigo": codigo,
        "nombre": nombre,
        "dni": dni,
        "categoria": categoria,
        "asunto": asunto,
        "estado": "Pendiente",
        "fecha_ingreso": fecha_ingreso_formateada
    }

    # Almacenar el expediente
    expedientes.append(nuevo_expediente)
    guardar_expedientes(expedientes)

    print("\n¡Expediente registrado correctamente!")
    print(f"Código generado: {codigo}")
    print(f"Categoría: {categoria}")
    print(f"Asunto: {asunto}")
    print(f"Fecha de ingreso: {fecha_ingreso_formateada}")
    print("Estado inicial: Pendiente")

