# Mesa de Partes Digital

Sistema de gestión de expedientes desarrollado en Python. Permite registrar, buscar, ordenar, actualizar y eliminar expedientes a través de un menú interactivo por consola.

## Descripción

Este programa simula una mesa de partes digital para el control y seguimiento de trámites presentados por ciudadanos. Cada expediente contiene el código, nombre del ciudadano, DNI, asunto y estado del trámite.

## Funcionalidades

- Registrar un nuevo expediente con validación de código único y formato de DNI.
- Buscar un expediente por su código.
- Buscar expedientes por DNI.
- Ordenar los expedientes por código.
- Mostrar la lista completa de expedientes.
- Actualizar el estado de un expediente (Pendiente, En proceso o Atendido).
- Eliminar un expediente previa confirmación.

## Requisitos

- Python 3.6 o superior

No se requieren librerías externas.

## Cómo ejecutar el programa

1. Abra una terminal en la carpeta del proyecto.
2. Ejecute el siguiente comando:

```bash
python mesa_de_partes.py
