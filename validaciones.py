
def validar_entero(mensaje):
    dato=input(mensaje)
    while(dato.isdigit()==False):
        dato=input("Dato incorrecto, intente nuevamente!: ")
    return int(dato)
def validar_decimal(mensaje):
    while(True):
        try:
            dato=float(input(mensaje))
            break;
        except:
            print('Error, ingrese un numero decimal')
    return dato
def validar_texto(mensaje):
    dato=input(mensaje).strip()
    while(len(dato)<2 or dato.replace(" ","").isalpha()==False):
        dato=input("Dato incorrecto, intente nuevamente!: ")
    return dato
documentos = set() #Almacena la informacion para que no se repita
def validar_documento(mensaje):
    dato = input(mensaje).strip()
    while not ((dato.isdigit) and 6 <= len(dato) <= 10 and dato[0] != '0' and len(set(dato)) > 1):
        dato = input('Documento incorrecto (solo numeros, de 6 a 10 digitos, sin empezar en 0): ').strip()
    return int(dato)
def validar_placa(mensaje):
    dato = input(mensaje).strip().upper()
    while not (dato.isalnum() and 5 <= len(dato) <= 7):
        dato = input('Placa incorrecta (5 a 7 letras o numeros): ').strip().upper()
    return dato
