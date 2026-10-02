import json
def cargar(nombre):
    with open(nombre, "r") as archivo:
        return json.load(archivo)


def guardar(nombre, datos):
    with open(nombre, "w") as archivo:
        json.dump(datos, archivo, indent=4)
def agregar_cita():
    clientes = cargar("clientes.json")
    instructores = cargar("instructores.json")
    citas = cargar("citas.json")

    id_cliente = int(input("ID cliente: "))
    id_instructor = int(input("ID instructor: "))

    cliente = next((x for x in clientes if x["id"] == id_cliente), None)
    instructor = next((x for x in instructores if x["id"] == id_instructor), None)

    if not cliente:
        print("Cliente no existe")
        return

    if not instructor:
        print("Instructor no existe")
        return

    if instructor["estado"] != "disponible":
        print("Instructor no disponible")
        return

    cita = {
        "id": len(citas) + 1,
        "id_cliente": id_cliente,
        "id_instructor": id_instructor,
        "fecha": input("Fecha: "),
        "hora": input("Hora: "),
        "estado": "pendiente"
    }

    citas.append(cita)
    guardar("citas.json", citas)

    print("Cita creada")


def listar_cita():
    citas = cargar("citas.json")

    for cita in citas:
        print(cita)


def actualizar_cita():
    citas = cargar("citas.json")

    id_cita = int(input("ID de la cita: "))

    for cita in citas:
        if cita["id"] == id_cita:
            cita["fecha"] = input("Nueva fecha: ")
            cita["hora"] = input("Nueva hora: ")
            cita["estado"] = input("Nuevo estado: ")

            guardar("citas.json", citas)
            print("Cita actualizada")
            return

    print("Cita no encontrada")


def eliminar_cita():
    citas = cargar("citas.json")

    id_cita = int(input("ID de la cita: "))

    for cita in citas:
        if cita["id"] == id_cita:
            citas.remove(cita)
            guardar("citas.json", citas)
            print("Cita eliminada")
            return

    print("Cita no encontrada")