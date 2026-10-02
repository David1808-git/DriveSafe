
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
    if documentos.exist:
        input('el ')
