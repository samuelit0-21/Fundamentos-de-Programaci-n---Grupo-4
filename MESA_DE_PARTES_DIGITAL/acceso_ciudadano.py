# MESA DE PARTES DIGITAL
# Módulo de acceso para el ciudadano

def iniciar_sesion_ciudadano():
    """Solicita DNI y nombre del ciudadano para iniciar sesión."""
    print("\n--- ACCESO CIUDADANO ---")

    dni = input("Ingrese su DNI: ").strip()
    nombre = input("Ingrese su nombre completo: ").strip()

    print("\nDatos ingresados:")
    print(f"DNI: {dni}")
    print(f"Nombre: {nombre}")
    print("\n(Solicitud registrada. Validaciones y menú ciudadano se implementarán a continuación.)")
