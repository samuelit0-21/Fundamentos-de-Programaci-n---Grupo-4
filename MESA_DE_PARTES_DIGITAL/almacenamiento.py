# MESA DE PARTES DIGITAL

import json
from pathlib import Path

# Ruta del archivo donde se guardaran los expedientes
ARCHIVO_EXPEDIENTES = Path(__file__).with_name("expedientes.json")


def guardar_expedientes(expedientes):
    """Guarda los expedientes en un archivo JSON."""
    with open(ARCHIVO_EXPEDIENTES, "w", encoding="utf-8") as archivo:
        json.dump(expedientes, archivo, ensure_ascii=False, indent=4)
    print("Expedientes guardados correctamente.")


def cargar_expedientes():
    """Carga los expedientes almacenados en el archivo JSON."""

    if not ARCHIVO_EXPEDIENTES.exists():
        guardar_expedientes([])
        return []

    with open(ARCHIVO_EXPEDIENTES, "r", encoding="utf-8") as archivo:
        expedientes = json.load(archivo)

    if not isinstance(expedientes, list):
        raise ValueError("El archivo de expedientes debe contener una lista.")

    return expedientes
