# Mesa de Partes Digital

# Expedientes de ejemplo
expedientes = [
    {
        "codigo": "EXP001",
        "nombre": "Juan Perez",
        "dni": "12345678",
        "asunto": "Solicitud de informacion"
    },
    {
        "codigo": "EXP002",
        "nombre": "Maria Lopez",
        "dni": "87654321",
        "asunto": "Solicitud de licencia"
    },
    {
        "codigo": "EXP003",
        "nombre": "Ana Torres",
        "dni": "45612378",
        "asunto": "Reclamo administrativo"
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
        "asunto": asunto
    }

    expedientes.append(nuevo_expediente)

    print("Expediente registrado correctamente.")
    
# 2. Buscar un expediente
def buscar_expediente():
    print("\n--- BUSCAR EXPEDIENTE ---")

    codigo = input("Ingrese el codigo que desea buscar: ").strip().upper()
    encontrado = False

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("\nExpediente encontrado:")
            print("Codigo:", expediente["codigo"])
            print("Ciudadano:", expediente["nombre"])
            print("DNI:", expediente["dni"])
            print("Asunto:", expediente["asunto"])

            encontrado = True
            break

    if encontrado == False:
        print("No se encontro el expediente.")
# 3. Ordenar expedientes por codigo
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

# 4. Mostrar todos los expedientes
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

# 5. Menu principal
def menu():
    while True:
        print("\n===== MESA DE PARTES DIGITAL =====")
        print("1. Registrar expediente")
        print("2. Buscar expediente")
        print("3. Ordenar expedientes")
        print("4. Mostrar expedientes")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_expediente()

        elif opcion == "2":
            buscar_expediente()

        elif opcion == "3":
            ordenar_expedientes()

        elif opcion == "4":
            mostrar_expedientes()

        elif opcion == "5":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")

#Iniciar el programa
menu()
