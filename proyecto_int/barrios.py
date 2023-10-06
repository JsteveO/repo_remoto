import readcsv as datos #leemos los datos del csv convertido en lista diccionario
from datetime import datetime #para trabajar con tiempo

datos = datos.read_csv('./proyecto_int/Proyecto_csv.csv') #llamamos el origen de los datos



seleccion = input("Ingrese su nombre => ")

def asesor(data):
    filtro = list(filter(lambda i: i['ASESOR_CIERRE'] == seleccion, data)) 
    '''lambda - filtra lo que se ingresó en el input _ itera en la columna asesor del origen data que posteriormente _
    se especifica de la varibale datos'''

    ultima_fecha = max([datetime.strptime(d['FECHA_DESEMBOLSO'], '%d/%m/%Y') for d in filtro]) #busca el últ día rgstrdo
    ultimo_mes = ultima_fecha.strftime('%m/%Y') #convierte en mes-año el útlimo día registrado en el origen de datos

    # Usamos un conjunto para garantizar la unicidad
    barrios_ultimo_mes = set()
    barrios_otros_meses = set()

    #ahora iteramos sobre los datos filtrados
    for dato in filtro:

        fecha_corte = datetime.strptime(dato['FECHA_DESEMBOLSO'], '%d/%m/%Y')
        mes_corte = fecha_corte.strftime('%m/%Y') #toma los meses de las fechas para crear condicional

        if mes_corte == ultimo_mes:
            barrios_ultimo_mes.add(dato['BARRIO_NEGOCIO']) #añade los barrios de los meses que son iguales al últ mes
        else:
            barrios_otros_meses.add(dato['BARRIO_NEGOCIO']) #añade los que son diferentes al último mes
    
    #convierte en listas
    l_ultimo_mes = list(barrios_ultimo_mes)
    l_otros_meses = list(barrios_otros_meses)

    return(l_ultimo_mes,l_otros_meses)


ultimo, otros = asesor(datos)

print(f'los barrios de octubre fueron {ultimo}')
print(f'los barrios de otras fechas fueron {otros}')

