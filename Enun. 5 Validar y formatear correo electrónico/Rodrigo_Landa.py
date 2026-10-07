def procesar_email(email):
    email_limpio = email.strip().lower()
    
    if "@" in email_limpio and "." in email_limpio:
        dominio = email_limpio.split("@")[1]
        return f"Email válido. Dominio: {dominio}"
    else:
        return "Email inválido."
#
print(procesar_email("   Usuario.Prueba@gmail.com   "))
