from validaciones import validar_entero
from menu_auxiliar import menu_administrador, menu_cliente, menu_instructor
from citas import listar_cita
def menu():
    while(True):
        opcion=validar_entero("""
                    BIENVENIDO AL CURSO DE CONDUCCION DAVID'S
                    Digite la opción:
                    1- Administrador
                    2- Instructor
                    3- Cliente
                    4- Salir.
                    """)
        match(opcion):
            case 1:
                clave=1234
                ingreso=validar_entero("ingrese la clave del administrador: ")
                while ingreso!= clave:
                    ingreso=validar_entero("clave incorrecta intente nuevamente: ")
                print("clave correcta bienvenido")
                menu_administrador()
            case 2:
                clave=2008
                ingreso=validar_entero("ingrese la clave del instructor: ")
                while ingreso!= clave:
                    ingreso=validar_entero("clave incorrecta intente nuevamente: ")
                print("clave correcta bienvenido")
                menu_instructor()
            case 3:
                clave=5678
                ingreso=validar_entero("ingrese la clave del cliente: ")
                while ingreso!= clave:
                    ingreso=validar_entero("clave incorrecta intente nuevamente: ")
                
                menu_cliente()
               
            case 4:
                print('Gracias por usar el aplicativo')
                break
            case _:
                print('Opcion no encontrada')