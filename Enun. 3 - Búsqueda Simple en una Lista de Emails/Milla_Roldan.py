# Lista de correos electrónicos.
emails = [
    "ana@gmail.com",
    "luis@outlook.com",
    "mia@gmail.com",
    "juan@yahoo.com"
]

# El contador comienza en cero.
cantidad_gmail = 0

# Recorremos cada correo de la lista.
for email in emails:
    # endswith() comprueba si el texto termina con lo indicado.
    if email.endswith("@gmail.com"):
        # Aumentamos el contador por cada correo de Gmail.
        cantidad_gmail += 1

# Mostramos cuántos correos son de Gmail.
print("Cantidad de emails de Gmail:", cantidad_gmail)

# \n agrega un salto de línea.
print("\nEmails que terminan en '.com':")

# Recorremos nuevamente los correos.
for email in emails:
    # Mostramos únicamente los que terminan en .com.
    if email.endswith(".com"):
        print(email)

# in verifica si este correo está dentro de la lista.
if "luis@outlook.com" in emails:
    print("\nEl email de Luis está en la lista.")
else:
    print("\nEl email de Luis no está en la lista.")
