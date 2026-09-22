#Enunciado:
#Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
#Realiza: (1) Agregar "Pedro Ruiz", (2) Buscar "Carlos Díaz" y mostrar posición, (3) Modificar "Luis Torres" por "Luis Mendoza", (4) Eliminar "Ana García".

Agenda = ["Ana Garcia","Luis Torres","Carlos Diaz","Maria Lopez"]

print(f"Mostramos la lista original: {Agenda}")

#Agregamos pedro ruiz

Agenda.append("Pedro Ruiz")

print (f"Mostramos la lista modificada: {Agenda}")

#Buscamos "Carlos Diaz" y mostramos posicion 

pos = Agenda.index("Carlos Diaz")

print(f"Mostramos la posicion de Carlos Diaz: {pos}")

#Modificamos "Luis torres" por "Luis Mendoza"
#Por indice

Agenda[1] = "Luis mendoza"

print(f"Mostramos el cambio de Luis Torres por Luis Mendoza:{Agenda}")

#Por condicion


for i in range(len(Agenda)):
    if Agenda[i] == "Luis Torres":
        Agenda[i] = "Luis mendoza"

print(f"Mostramos el cambio de Luis Torres por Luis Mendoza:{Agenda}")

#Eliminamos "Ana Garcia" 

#Agenda.remove("Ana Garcia")

print(f"Aqui se muestra la lista donde se ha removido Ana Garcia: {Agenda}")

#remove nos sirve para remover por el conteniodo, en este caso el contenido seria "Ana Garcia"

# del Agenda[0]

print(f"Aqui se muestra la lista donde se ha eliminado Ana Garcia: {Agenda}")

#del a diferencia de remove se encarga de eliminar el contenido por indice

eliminado = Agenda.pop(0)

print(f"Mostramos la lista donde se ha removido Ana Garcia: {Agenda}")
print(f"Elemento eliminado: {eliminado}")

#Como final imprimimos la lista final

print(Agenda)
