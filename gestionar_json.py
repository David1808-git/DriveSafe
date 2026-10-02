import os
import json

def cargar(nombre_archivo):
    try:#lanza la aplicacion
        #accede de una al path del proyecto y dentro del proyecto debe haber un archivo con ese nombre
        if os.path.exists(nombre_archivo):#obtiene el path o ruta del arhivo "C://user/david/documents/bodemodas_kerem/productos.json"
            with open (nombre_archivo, 'r') as archivo:#abre el archivo json como una lectura 'read'
                return json.load(archivo)#retorna el json (lista de diccionarios)
        else:
            return []#no existe aun un json y por eso la lista que se muestra es vacia
    except json.JSONDecodeError as ex:
        print(ex)

def reemplazar(nombre_archivo, lista_datos):#recibe el nombre del json y la lista que va a reemplazar
    with open(nombre_archivo, 'w') as archivo:#se abre como escritura 'write'
        json.dump(lista_datos, archivo, indent=4)#guarda el json con los datos que tiene la lista
        #colocando un espaciado de 4. o 1 tap

def generar_id(lista):
    if not lista:
        return 1
    else:
        return lista[-1].get("id","0")+1

