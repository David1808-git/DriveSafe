from gestionar_json import cargar, reemplazar, generar_id
from fecha import fecha_hora_duracion


def agregar_cita():
    clientes = cargar("clientes.json")
    instructores = cargar("instructores.json")
    vehiculos=cargar("vehiculos.json")
    citas = cargar("citas.json")

    print("\n--- CLIENTES ---")

    for cliente in clientes:
        print(cliente["id"], "-", cliente["nombre"])

    id_cliente = int(input("Seleccione el ID del cliente: "))

    print("\n--- INSTRUCTORES ---")

    for instructor in instructores:
        print(instructor["id"], "-", instructor["nombre"])

    id_instructor = int(input("Seleccione el ID del instructor: "))
    for vehiculo in vehiculos:
        print(vehiculo["id"], "-", "", vehiculo["tipo_de_vehiculo"])
    tipo_de_vehiculo= str(input("seleccione el tipo de vehiculo: "))
    fecha,hora, duracion=fecha_hora_duracion()
    cita = {
    "id": generar_id(citas),
    "id_cliente": id_cliente,
    "id_instructor": id_instructor,
    "tipo_vehiculo": tipo_de_vehiculo,
    "fecha": fecha,
    "hora": hora,
    "duracion": duracion,
    "estado": "pendiente",
    "Observaciones": " en espera"
}

    citas.append(cita)

    reemplazar("citas.json", citas)

    print("Cita creada correctamente")


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
            cita["observaciones"]= input("Ingrese las observaciones")

            reemplazar("citas.json", citas)

            print("Cita actualizada")
            return

    print("Cita no encontrada")


def eliminar_cita():
    citas = cargar("citas.json")

    id_cita = int(input("ID de la cita: "))

    for cita in citas:
        if cita["id"] == id_cita:
            citas.remove(cita)

            reemplazar("citas.json", citas)

            print("Cita eliminada")
            return

    print("Cita no encontrada")