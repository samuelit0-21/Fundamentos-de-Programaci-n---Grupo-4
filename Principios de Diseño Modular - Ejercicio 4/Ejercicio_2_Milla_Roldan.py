def validar_email(email):
    return "@" in email and "." in email
def validar_password(pwd):
    return len(pwd) >= 8
def validar_formulario(email, pwd):
    return validar_email(email) and validar_password(pwd
