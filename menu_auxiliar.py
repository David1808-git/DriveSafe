from validaciones import validar_entero
from clientes import agregar_cliente, actualizar_cliente, listar_cliente,eliminar_cliente
from instructores import agregar_instructor, actualizar_instructor, listar_instructor, eliminar_instructor
from citas import agregar_cita, actualizar_cita, eliminar_cita, listar_cita
from vehiculos import agregar_vehiculo, actualizar_vehiculo, listar_vehiculos, eliminar_vehiculo
def menu_administrador():
    while (True):
        op1=validar_entero('''
                BIENVENIDO AL APARTADO DE ADMINISTRADOR                           
                                1.Gestionar Clientes
                                2.Gestionar Instructor
                                3.Gestionar Citas
                                4.Gestionar vehiculos
                                4.Regresar
''')
        match(op1):
            case 1:
                op2=validar_entero('''
                                        Ingrese la opcion a realizar
                                   1. Agregar cliente
                                   2. Actualizar cliente
                                   3. listar cliente
                                   4. Eliminar cliente
                                   5. Regresar                                        
''')
                match(op2):
                    case 1: 
                        agregar_cliente()
                    case 2:
                        listar_cliente()
                        id=validar_entero("Ingrese el id a actualizar: ")
                        actualizar_cliente(id)
                    case 3:
                        listar_cliente()
                    case 4:
                        listar_cliente()
                        id_borrar=validar_entero("Ingrese el id a eliminar: ")
                        eliminar_cliente(id_borrar)
                    case 5:
                        print('Regresando....')
                        break
                    case _: 
                        print('opcion no encontrada')
            case 2:
                op3=validar_entero('''
                           Ingrese la opcion a realizar
                                   1. Agregar instructor
                                   2. Actualizar instructor
                                   3. listar instructor
                                   4. Eliminar instructor
                                   5. Regresar                                        
''')
                match(op3):
                    case 1:
                        agregar_instructor()
                    case 2:
                        listar_instructor()
                        actualizar_instructor(id)
                    case 3:
                        listar_instructor()
                    case 4: 
                        listar_instructor()
                        eliminar_instructor(id)
                    case 5:
                        print('Regresando....')
                        break
                    case _: 
                        print('opcion no encontrada')
            
                
            case 3:
                op4=validar_entero('''
                           Ingrese la opcion a realizar
                                   1. Agregar cita
                                   2. Actualizar cit
                                   3. listar cita
                                   4. Eliminar cita
                                   5. Regresar                                        
''')
                match(op4):
                    case 1:
                        agregar_cita()
                    case 2:
                        listar_cita()
                        actualizar_cita(id)
                    case 3:
                        listar_cita()
                    case 4: 
                        listar_cita()
                        eliminar_cita(id)
                    case 5:
                        print('Regresando....')
                        break
                    case _: 
                        print('opcion no encontrada')
            case 4: 
                op5=validar_entero('''
                           Ingrese la opcion a realizar
                                   1. Agregar vehiculo
                                   2. Actualizar vehiculo
                                   3. listar vehiculo
                                   4. Eliminar vehiculo
                                   5. Regresar                                        
''')
                match(op5):
                    case 1:
                        agregar_vehiculo()
                    case 2:
                        listar_vehiculos()
                        actualizar_vehiculo(id)
                    case 3:
                        listar_vehiculos()
                    case 4: 
                        listar_vehiculos()
                        eliminar_vehiculo(id)
                    case 5:
                        print('Regresando....')
                        break
                    case _: 
                        print('opcion no encontrada')
            case 5:
                print('Regresando....')
                break
            case _: 
                print('Opcion no encontrada')
def menu_cliente():
    while(True):
        op=validar_entero('''
            Bienvenido al apartado de cliente
            escoja la opcion a realizar
            1. Ver mis citas
            2. Salir
    ''')
        match(op):
            case 1:
                listar_cita()
            case 2:
                print('Gracias por usar nuestros servicios')
                print('Regresando....')
                break
                

