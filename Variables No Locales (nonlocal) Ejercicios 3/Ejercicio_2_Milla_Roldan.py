# Ejercicio 2 — Acumulador
# Creamos la función principal.
def crear_acumulador():

    # Variable local de crear_acumulador().
    # Aquí guardaremos la suma acumulada.
    total = 0

    # Creamos una función interna que recibe un valor.
    def acumular(valor):

        # Indicamos que "total" pertenece a la función exterior.
        # Esto nos permite modificar su valor.
        nonlocal total

        # Sumamos el valor recibido al total existente.
        total += valor

        # Devolvemos el nuevo total.
        return total

    # Devolvemos la función interna "acumular".
    return acumular


# Creamos nuestro acumulador.
# "suma" ahora contiene la función interna acumular().
suma = crear_acumulador()

# Enviamos 10.
# total era 0, entonces:
# 0 + 10 = 10
print(suma(10))  # 10

# Enviamos 5.
# Como total conserva el valor 10:
# 10 + 5 = 15
print(suma(5))   # 15
