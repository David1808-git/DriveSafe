from datetime import date, datetime, timedelta

hoy=date.today()
ahora=datetime.now()

print(f'''
{hoy}
{ahora}
''')

#restar entre las fechas
vencimiento=date(2026,12,31)# para almacenar una fecha
creacion=datetime.strptime("1998-05-19", "%Y-%m-%d").date() #almacenar una fecha de creación desde su string

resta_dias=(creacion-vencimiento)
resta_años=resta_dias.days/365
print(f'''
{vencimiento}
{creacion}
{resta_dias}
{resta_años}
''')

#asignar una fecha futura
mañana=hoy+timedelta(days=1)
hace_una_semana=hoy-timedelta(weeks=1)
en_2_horas=ahora+timedelta(hours=2)
print(f'''
{mañana}
{hace_una_semana}
{en_2_horas}
''')
#comparacion
fecha_pago=date(2026,9,30)
if fecha_pago<hoy:
    dias_mora=(hoy-fecha_pago).days
    print(f'pago vnecido hace {dias_mora} dias')
elif fecha_pago==hoy:
    print('Vence hoy')
else:
    print('Al dia')