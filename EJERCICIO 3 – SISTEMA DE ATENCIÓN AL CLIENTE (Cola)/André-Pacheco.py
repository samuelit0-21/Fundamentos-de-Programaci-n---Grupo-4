cola_clientes = []

def tomar_turno(nombre_cliente):
    cola_clientes.append(nombre_cliente)
    print(f"Tomó turno: {nombre_cliente}")

def atender():
    if len(cola_clientes) > 0:
        cliente_atendido = cola_clientes.pop(0)
        print(f"Cliente atendido: {cliente_atendido}")
    else:
        print("No hay clientes esperando en la cola.")

def mostrar_cola():
    print(f"Clientes esperando ({len(cola_clientes)}): {cola_clientes}")

#Enunciado
print("=== EJERCICIO 3: SISTEMA DE TURNOS DEL BANCO ===")

#Entran los clientes
tomar_turno("Gabriel")
tomar_turno("Sofia")
tomar_turno("Mateo")
tomar_turno("Valeria")
mostrar_cola()

#Atención a clientes
print("\n--- ATENDIENDO PRIMEROS 2 CLIENTES ---")
atender()
atender()
mostrar_cola()

#Entre un cliente
print("\n--- INGRESA UN NUEVO CLIENTE ---")
tomar_turno("Diego")
mostrar_cola()

#Atención de los demás
print("\n--- ATENDIENDO A TODOS LOS RESTANTES ---")
while len(cola_clientes) > 0:
    atender()

mostrar_cola()
