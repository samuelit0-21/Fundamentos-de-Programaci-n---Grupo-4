
# MESA DE PARTES DIGITAL

# Expedientes de ejemplo
expedientes = [
    {
        "codigo": "EXP001",
        "nombre": "Juan Perez",
        "dni": "12345678",
        "asunto": "Solicitud de informacion",
        "estado": "Pendiente"
    },
    {
        "codigo": "EXP002",
        "nombre": "Maria Lopez",
        "dni": "87654321",
        "asunto": "Solicitud de licencia",
        "estado": "Pendiente"
    },
    {
        "codigo": "EXP003",
        "nombre": "Ana Torres",
        "dni": "45612378",
        "asunto": "Reclamo administrativo",
        "estado": "Pendiente"
    }
]

# 1. Registrar un expediente
def registrar_expediente():
    print("\n--- REGISTRAR EXPEDIENTE ---")

    codigo = input("Ingrese el codigo: ").strip().upper()

    # Verificamos que el codigo no se repita
    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("Error: el codigo ya existe.")
            return

    nombre = input("Ingrese el nombre del ciudadano: ").strip()
    dni = input("Ingrese el DNI: ").strip()
    asunto = input("Ingrese el asunto: ").strip()

    # Validamos los datos
    if codigo == "" or nombre == "" or dni == "" or asunto == "":
        print("Error: todos los campos son obligatorios.")
        return

    if len(dni) != 8 or not dni.isdigit():
        print("Error: el DNI debe tener 8 numeros.")
        return

    # Creamos el expediente
    nuevo_expediente = {
        "codigo": codigo,
        "nombre": nombre,
        "dni": dni,
        "asunto": asunto,
        "estado": "Pendiente"
    }

    expedientes.append(nuevo_expediente)

    print("Expediente registrado correctamente.")


# 2. Buscar un expediente por codigo
def buscar_expediente():
    print("\n--- BUSCAR EXPEDIENTE POR CODIGO ---")

    codigo = input("Ingrese el codigo que desea buscar: ").strip().upper()
    encontrado = False

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("\nExpediente encontrado:")
            print("Codigo:", expediente["codigo"])
            print("Ciudadano:", expediente["nombre"])
            print("DNI:", expediente["dni"])
            print("Asunto:", expediente["asunto"])
            print("Estado:", expediente["estado"])

            encontrado = True
            break

    if encontrado == False:
        print("No se encontro el expediente.")


# 3. Buscar expediente por DNI
def buscar_por_dni():
    print("\n--- BUSCAR EXPEDIENTE POR DNI ---")

    dni = input("Ingrese el DNI del ciudadano: ").strip()

    # Validamos que el DNI tenga 8 numeros
    if len(dni) != 8 or not dni.isdigit():
        print("Error: el DNI debe tener 8 numeros.")
        return

    encontrado = False

    # Buscamos los expedientes asociados al DNI
    for expediente in expedientes:
        if expediente["dni"] == dni:

            print("\nExpediente encontrado:")
            print("Codigo:", expediente["codigo"])
            print("Ciudadano:", expediente["nombre"])
            print("DNI:", expediente["dni"])
            print("Asunto:", expediente["asunto"])
            print("Estado:", expediente["estado"])

            encontrado = True

    if encontrado == False:
        print("No se encontraron expedientes para este DNI.")


# 4. Ordenar expedientes por codigo
def ordenar_expedientes():
    print("\n--- ORDENAR EXPEDIENTES ---")

    for i in range(len(expedientes)):
        for j in range(0, len(expedientes) - i - 1):
            if expedientes[j]["codigo"] > expedientes[j + 1]["codigo"]:
                temporal = expedientes[j]
                expedientes[j] = expedientes[j + 1]
                expedientes[j + 1] = temporal

    print("Expedientes ordenados por codigo.")
    mostrar_expedientes()


# 5. Mostrar todos los expedientes
def mostrar_expedientes():
    print("\n--- LISTA DE EXPEDIENTES ---")

    if len(expedientes) == 0:
        print("No hay expedientes registrados.")
        return

    for expediente in expedientes:
        print("-----------------------------")
        print("Codigo:", expediente["codigo"])
        print("Ciudadano:", expediente["nombre"])
        print("DNI:", expediente["dni"])
        print("Asunto:", expediente["asunto"])
        print("Estado:", expediente["estado"])


# 6. Actualizar el estado del expediente
def actualizar_estado():
    print("\n--- ACTUALIZAR ESTADO DEL EXPEDIENTE ---")

    codigo = input("Ingrese el codigo del expediente: ").strip().upper()

    # Buscamos el expediente
    for expediente in expedientes:
        if expediente["codigo"] == codigo:

            print("\nExpediente encontrado.")
            print("Seleccione el nuevo estado:")
            print("1. Pendiente")
            print("2. En proceso")
            print("3. Atendido")

            opcion = input("Ingrese la opcion: ").strip()

            if opcion == "1":
                expediente["estado"] = "Pendiente"

            elif opcion == "2":
                expediente["estado"] = "En proceso"

            elif opcion == "3":
                expediente["estado"] = "Atendido"

            else:
                print("Error: opcion no valida.")
                return

            print("Estado actualizado correctamente.")
            print("Nuevo estado:", expediente["estado"])
            return

    print("Error: el expediente no existe.")


# 7. Eliminar un expediente
def eliminar_expediente():
    print("\n--- ELIMINAR EXPEDIENTE ---")

    codigo = input("Ingrese el codigo del expediente a eliminar: ").strip().upper()

    encontrado = None

    # Buscamos el expediente
    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            encontrado = expediente
            break

    if encontrado is None:
        print("No se encontro el expediente.")
        return

    # Mostramos los datos del expediente
    print("\nExpediente encontrado:")
    print("Codigo:", encontrado["codigo"])
    print("Ciudadano:", encontrado["nombre"])
    print("DNI:", encontrado["dni"])
    print("Asunto:", encontrado["asunto"])
    print("Estado:", encontrado["estado"])

    # Solicitar confirmación al usuario
    confirmacion = input("\n¿Desea eliminar este expediente? (S/N): ").strip().upper()
    
    # Eliminar o conservar según la respuesta
    if confirmacion == "S" or confirmacion == "SI":
        expedientes.remove(encontrado)
        print("Expediente eliminado correctamente.")          # Mensaje de éxito
    else:
        print("Operacion cancelada. El expediente no fue eliminado.")  # Mensaje de cancelación


# 8. Menu principal
def menu():
    while True:
        print("\n===== MESA DE PARTES DIGITAL =====")
        print("1. Registrar expediente")
        print("2. Buscar expediente por codigo")
        print("3. Buscar expediente por DNI")
        print("4. Ordenar expedientes")
        print("5. Mostrar expedientes")
        print("6. Actualizar estado del expediente")
        print("7. Eliminar expediente")
        print("8. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_expediente()

        elif opcion == "2":
            buscar_expediente()

        elif opcion == "3":
            buscar_por_dni()

        elif opcion == "4":
            ordenar_expedientes()

        elif opcion == "5":
            mostrar_expedientes()

        elif opcion == "6":
            actualizar_estado()

        elif opcion == "7":
            eliminar_expediente()

        elif opcion == "8":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")


# Iniciar el programa
menu()

