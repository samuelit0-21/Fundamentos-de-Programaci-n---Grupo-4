# Mesa de Partes Digital

Sistema de gestión de expedientes municipales desarrollado en Python. Permite registrar, consultar, modificar, eliminar y actualizar el estado de trámites y solicitudes de una mesa de partes digital, con almacenamiento permanente en archivo JSON.

## Autores

- **Dalessandro Nina**
- **Samuel Milla**
- **Rodrigo Landa**

## Descripción

**Mesa de Partes Digital** es un sistema de consola que simula la gestión de una mesa de partes municipal. Los ciudadanos pueden presentar solicitudes clasificadas por categorías, y el sistema genera códigos únicos, registra fechas de ingreso y permite el seguimiento completo de cada expediente (desde su registro hasta su atención).

El proyecto está modularizado para facilitar el mantenimiento y la comprensión del código.

## Características principales

- Registro de expedientes con código único automático (`EXP-AAAA-XXXXXX`)
- Selección de categorías y trámites sugeridos
- Búsqueda de expedientes por código, DNI o nombre
- Listado completo de expedientes registrados
- Ordenamiento de expedientes por código (método burbuja)
- Modificación de datos de un expediente
- Eliminación de expedientes (con confirmación)
- Actualización de estado (`Pendiente`, `En proceso`, `Atendido`)
- Persistencia automática de datos en archivo JSON
- Validaciones de campos (DNI de 8 dígitos, campos obligatorios, etc.)

## Categorías de trámites

1. **Tributarios y prediales**  
   (Consulta de impuesto predial, arbitrios, fraccionamiento, reclamos tributarios)

2. **Documentación y constancias municipales**  
   (Constancias, copias de documentos, información municipal)

3. **Solicitudes administrativas municipales**  
   (Solicitudes a áreas, presentación de documentos, atención administrativa)

4. **Reclamos y consultas**  
   (Reclamos por servicios municipales, limpieza pública, parques, etc.)

5. **Otros trámites**  
   (Permite describir una solicitud personalizada)

## Requisitos

- Python 3.7 o superior
- No requiere librerías externas (solo módulos estándar)

## Instalación y ejecución

1. Clona o descarga el repositorio.
2. Asegúrate de que todos los archivos estén en la misma carpeta.
3. Ejecuta el programa desde la terminal:

```bash
python main.py
```

## Estructura del proyecto

```
.
├── main.py                      # Menú principal y control del programa
├── registros.py                 # Registro de nuevos expedientes
├── consultas.py                 # Búsquedas (código, DNI, nombre) y listado
├── modificaciones.py            # Modificación de datos de expedientes
├── eliminaciones.py             # Eliminación de expedientes
├── actualizacion_estado.py      # Actualización del estado del expediente
├── ordenamiento.py              # Ordenamiento por código (burbuja)
├── almacenamiento.py            # Funciones para guardar y cargar JSON
├── datos.py                     # Carga inicial de la lista de expedientes
└── expedientes.json             # Archivo de almacenamiento de datos
```

## Menú principal

Al ejecutar el programa se muestra el siguiente menú:

1. Registrar expediente  
2. Buscar expediente por código  
3. Ordenar expedientes por código  
4. Buscar expediente por nombre  
5. Mostrar todos los expedientes  
6. Buscar expediente por DNI  
7. Modificar datos del expediente  
8. Eliminar expediente  
9. Actualizar estado del expediente  
10. Salir  

## Funcionamiento general

- Cada operación que modifica datos (registro, modificación, eliminación o cambio de estado) guarda automáticamente los cambios en `expedientes.json`.
- El código de expediente se genera de forma aleatoria y se verifica que no exista previamente.
- Los estados posibles de un expediente son: **Pendiente**, **En proceso** y **Atendido**.
- El sistema realiza validaciones básicas de entrada (campos vacíos, formato de DNI, opciones válidas).

## Notas

Este es un proyecto académico desarrollado con fines educativos. Está pensado para demostrar modularización, manejo de archivos JSON, estructuras de control y buenas prácticas básicas en Python.

---

**Mesa de Partes Digital** — Proyecto grupal en Python
