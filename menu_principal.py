from validaciones import validar_entero
from menu_auxiliar import menu_administrador, menu_cliente
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
                print('Bienvenido al sistema')
               
            case 3:
                menu_cliente()
               
            case 4:
                print('Gracias por usar el aplicativo')
                break
            case _:
                print('Opcion no encontrada')