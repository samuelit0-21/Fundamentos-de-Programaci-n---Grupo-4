# Importamos el módulo para trabajar con expresiones regulares.
import re

# Cada texto contiene nombre, edad y teléfono.
registros = [
    "Ana García - edad:25 - tel:987654321",
    "Luis Pérez - edad:30 - tel:912345678"
]

# Aquí guardaremos los datos extraídos.
personas = []

# Los paréntesis crean tres grupos para capturar los datos.
# (.+?) captura el nombre.
# \s* permite espacios opcionales alrededor de los separadores.
# (\d+) captura uno o más dígitos para edad y teléfono.
# La r antes del texto indica una cadena cruda para escribir la regex.
patron = r"(.+?)\s*-\s*edad:(\d+)\s*-\s*tel:(\d+)"

# Revisamos cada registro.
for registro in registros:
    # fullmatch() verifica que todo el registro tenga el formato esperado.
    coincidencia = re.fullmatch(patron, registro)

    # Solo extraemos los datos si encontramos una coincidencia.
    if coincidencia:
        personas.append({
            # group(1) obtiene el nombre y strip() quita espacios externos.
            "nombre": coincidencia.group(1).strip(),

            # group(2) obtiene la edad y la convertimos a entero.
            "edad": int(coincidencia.group(2)),

            # group(3) obtiene el teléfono.
            # Lo dejamos como texto para conservar posibles ceros iniciales.
            "telefono": coincidencia.group(3)
        })

# Mostramos los diccionarios creados.
for persona in personas:
    print(persona)
