from gestionar_json import generar_id, reemplazar, cargar
from validaciones import validar_texto, validar_entero, validar_placa
NOMBRE_ARCHIVO="vehiculos.json"
def agregar_vehiculo():
    lista_vehiculos=[]
    lista_vehiculos=cargar(NOMBRE_ARCHIVO)
    vehiculos={}
    vehiculos["id"]=generar_id(lista_vehiculos)
    vehiculos["tipo_de_vehiculo"]=validar_texto('Ingrese el tipo de vehiculo ejp: Carro o Moto: ')
    vehiculos["placa"]=validar_placa('Ingrese la placa del vehiculo: ')
    vehiculos["estado"]=validar_texto('Ingrese el estado del vehiculo: ')
    lista_vehiculos.append(vehiculos)
    reemplazar(NOMBRE_ARCHIVO, lista_vehiculos)
    print("vehiculo creado correctamente!")
def actualizar_vehiculo(id):
    lista_vehiculos=cargar(NOMBRE_ARCHIVO)
    for i,elemento in enumerate(lista_vehiculos): #recorre los diccionarios que contiene la lista
            if(elemento["id"]==id):
                op=validar_entero(""""
                                Digite lo que desea actualizar:
                                1- estado
                                """)
                match(op):
                    case 1:
                        elemento["estado"]=validar_texto("Ingrese el nuevo estado: ")
                        reemplazar(NOMBRE_ARCHIVO, lista_vehiculos)
                        print('esatdo actualizado correctamente!')
                    
                    case _:
                        print("Opcion no correcta, operación cancelada!")
def eliminar_vehiculo(id):
    validacion=False
    lista_vehiculos=cargar(NOMBRE_ARCHIVO)
    for i,elemento in enumerate(lista_vehiculos): #recorre los diccionarios que contiene la lista
            if(elemento["id"]==id):
                lista_vehiculos.pop(i)
                reemplazar(NOMBRE_ARCHIVO, lista_vehiculos)
                print('Dato eliminado correctamente!')
                validacion=True
                break
    if validacion==False:
        print("El id no existe!") 
def listar_vehiculos():
    lista_vehiculos=cargar(NOMBRE_ARCHIVO)
    for i,elemento in enumerate(lista_vehiculos): #recorre los diccionarios que contiene la lista
            print(f'''
                ********************
                ID:         {elemento.get("id", "La clave id no existe")}
                Tipo_de_vehiculo:     {elemento.get("tipo de vehiculo", "La clave tipo de vehiculo no existe")}
                Placa: {elemento.get('placa', 'la clave placa no existe')}
                Estado: {elemento.get("estado", 'la calve estado no existe')}
            ''')