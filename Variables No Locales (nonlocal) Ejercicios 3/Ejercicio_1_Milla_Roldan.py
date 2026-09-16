# Ejercicio 1 — Generador de IDs
# Creamos una función principal llamada generador_id.
def generador_id():

    # Variable local de generador_id().
    # Guardará el último número de ID generado.
    ultimo_id = 0

    # Creamos una función interna.
    # Esta función será la encargada de generar cada nuevo ID.
    def nuevo_id():

        # nonlocal indica que queremos utilizar y modificar
        # la variable "ultimo_id" de la función generador_id().
        nonlocal ultimo_id

        # Aumentamos el último ID en 1.
        ultimo_id += 1

        # Devolvemos el ID como texto.
        # :04d hace que el número tenga 4 dígitos,
        # agregando ceros a la izquierda cuando sea necesario.
        return f"ID-{ultimo_id:04d}"

    # Devolvemos la función interna.
    # No usamos paréntesis porque queremos devolver la función,
    # no ejecutarla todavía.
    return nuevo_id


# Ejecutamos generador_id() y guardamos
# la función nuevo_id dentro de "gen".
gen = generador_id()

# Ejecutamos la función guardada en "gen".
# ultimo_id pasa de 0 a 1.
print(gen())  # ID-0001

# La ejecutamos nuevamente.
# ultimo_id conserva su valor anterior y pasa de 1 a 2.
print(gen())  # ID-0002
