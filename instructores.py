from gestionar_json import generar_id, reemplazar, cargar
from validaciones import validar_texto, validar_entero
NOMBRE_ARCHIVO="instructores.json"
def agregar_instructor():
    lista_instructores=[]
    lista_instructores=cargar(NOMBRE_ARCHIVO)
    instructor={}
    instructor["id"]=generar_id(lista_instructores)
    instructor["nombre"]=validar_texto("Ingrese el nombre del instructor: ")
    instructor["documento"]=validar_entero("ingrese su documento: ")
    instructor["tipo de vehiculo"]=validar_texto("Ingrese el vehiculo experto ejp:(carro o moto): ")
    instructor["estado"]=validar_texto('Ingrese su estado ejp: ocupado o disponible: ')
    lista_instructores.append(instructor)
    reemplazar(NOMBRE_ARCHIVO, lista_instructores)
    print("Instructor creado correctamente!")
def actualizar_instructor(id):
    lista_instructor=cargar(NOMBRE_ARCHIVO)
    for i,elemento in enumerate(lista_instructor): #recorre los diccionarios que contiene la lista
            if(elemento["id"]==id):
                op=validar_entero(""""
                                Digite lo que desea actualizar:
                                1- Nombre.
                                """)
                match(op):
                    case 1:
                        elemento["nombre"]=validar_texto("Ingrese el nuevo nombre: ")
                        reemplazar(NOMBRE_ARCHIVO, lista_instructor)
                        print('Nombre actualizado correctamente!')
                    
                    case _:
                        print("Opcion no correcta, operación cancelada!")
def eliminar_instructor(id):
    validacion=False
    lista_instructores=cargar(NOMBRE_ARCHIVO)
    for i,elemento in enumerate(lista_instructores): #recorre los diccionarios que contiene la lista
            if(elemento["id"]==id):
                lista_instructores.pop(i)
                reemplazar(NOMBRE_ARCHIVO, lista_instructores)
                print('Dato eliminado correctamente!')
                validacion=True
                break
    if validacion==False:
        print("El id no existe!") 
def listar_instructor():
    lista_instructores=cargar(NOMBRE_ARCHIVO)
    for i,elemento in enumerate(lista_instructores): #recorre los diccionarios que contiene la lista
            print(f'''
                ********************
                ID:         {elemento.get("id", "La clave id no existe")}
                Nombre:     {elemento.get("nombre", "La clave nombre no existe")}
                Descripcion:     {elemento.get("descripcion", "La clave descripcion no existe")}
            ''')