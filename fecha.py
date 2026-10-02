from datetime import datetime
from validaciones import validar_entero
def fecha_hora_duracion():
    while True:
        fecha=input('Ingrese la fecha en la que desea realizar la clase: (DD/MM/AAAA): ')
        try:
            fecha_valida=datetime.strptime(fecha, "%d/%m/%Y")
            break
        except ValueError:
            print ('Error al ingresar la fecha, intente nuevamente: ')
    while True:
            hora=input('Ingrese la hora en la que desea realizar la clase: (HH:MM formato 24h ej: 20:30): ')
            try:
                hora_valida=datetime.strptime(hora, "%H:%M")
                break
            except ValueError:
                print ('Error al ingresar la hora, intente nuevamente: ')
    while True:
            duracion=validar_entero('Ingrese la duracion de la clase en minutos (ej:30): ')
            break
    return fecha, hora, duracion