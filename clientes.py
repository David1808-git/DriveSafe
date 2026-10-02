from gestionar_json import generar_id, reemplazar, cargar
from validaciones import validar_texto, validar_entero, validar_documento
NOMBRE_ARCHIVO="clientes.json"
def agregar_cliente():
    lista_clientes=[]
    lista_clientes=cargar(NOMBRE_ARCHIVO)
    cliente={}
    cliente["id"]=generar_id(lista_clientes)
    cliente["nombre"]=validar_texto("Ingrese el nombre del cliente: ")
    cliente["documento"]=validar_documento("ingrese su documento: ")
    cliente["tipo de vehiculo"]=validar_texto("Ingrese el vehiculo: ")
    lista_clientes.append(cliente)
    reemplazar(NOMBRE_ARCHIVO, lista_clientes)
    print("cliente creado correctamente!")
def actualizar_cliente(id):
    lista_clientes=cargar(NOMBRE_ARCHIVO)
    for i,elemento in enumerate(lista_clientes): #recorre los diccionarios que contiene la lista
            if(elemento["id"]==id):
                op=validar_entero(""""
                                Digite lo que desea actualizar:
                                1- Nombre.
                                """)
                match(op):
                    case 1:
                        elemento["nombre"]=validar_texto("Ingrese el nuevo nombre: ")
                        reemplazar(NOMBRE_ARCHIVO, lista_clientes)
                        print('Nombre actualizado correctamente!')
                    
                    case _:
                        print("Opcion no correcta, operación cancelada!")
def eliminar_cliente(id):
    validacion=False
    lista_clientes=cargar(NOMBRE_ARCHIVO)
    for i,elemento in enumerate(lista_clientes): #recorre los diccionarios que contiene la lista
            if(elemento["id"]==id):
                lista_clientes.pop(i)
                reemplazar(NOMBRE_ARCHIVO, lista_clientes)
                print('Dato eliminado correctamente!')
                validacion=True
                break
    if validacion==False:
        print("El id no existe!") 
def listar_cliente():
    lista_clientes=cargar(NOMBRE_ARCHIVO)
    for i,elemento in enumerate(lista_clientes): #recorre los diccionarios que contiene la lista
            print(f'''
                ********************
                ID:         {elemento.get("id", "La clave id no existe")}
                Nombre:     {elemento.get("nombre", "La clave nombre no existe")}
                Tipo vehiculo:     {elemento.get("tipo vehiculo", "La clave tipo vehiculo no existe no existe")}
            ''')