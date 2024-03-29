import readcsv as datos #leemos los datos del csv convertido en lista diccionario
from datetime import datetime #para trabajar con tiempo
import pandas as pd

datos = datos.read_csv('./proyecto_int/Proyecto_csv.csv') #llamamos el origen de los datos



seleccion = input("Ingrese su nombre => ")

wpp = int(input("Ver Barrios = > 1, ver Clientes = > 2"))

if wpp == 1:

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

            barrios_ = dato.get('BARRIO_NEGOCIO')
            municipios_ = dato.get('MUNICIPIO_NEGOCIO')
            #saldo_ = dato.get(' SALDO_CORTE ')

            if mes_corte == ultimo_mes:
                #barrios_ultimo_mes.add(dato['BARRIO_NEGOCIO']) #añade los barrios de los meses que son iguales al últ mes
                barrios_ultimo_mes.add((barrios_,municipios_))
            else:
                #barrios_otros_meses.add(dato['BARRIO_NEGOCIO']) #añade los que son diferentes al último mes
                barrios_otros_meses.add((barrios_,municipios_))
        #convierte en listas
        l_ultimo_mes = list(barrios_ultimo_mes)
        l_otros_meses = list(barrios_otros_meses)

        return(l_ultimo_mes,l_otros_meses)


    ultimo, otros = asesor(datos)

    print(f'los barrios de octubre fueron {ultimo}')
    print(f'los barrios de otras fechas fueron {otros}')


# barrios con monto


else:
#clientes con deuda baja

    def asesor2(data2):
        filtro = list(filter(lambda i: i['ASESOR_CIERRE'] == seleccion, data2))
        filtro2 = list(filter(lambda i: i['PEOR_CALIFICACION'] in ['A', 'B', 'C'] 
        and (int(i['MONTO_DESEMBOLSADO']) * 0.10) > int(i[' SALDO_CORTE ']), filtro))

        resultados = []

        for i in filtro2:
            resultado = [
            i['APELLIDOS_NOMBRES'],
            i['MUNICIPIO_NEGOCIO'],
            i['BARRIO_NEGOCIO'],
            i[' SALDO_CORTE ']
            ]
            resultados.append(resultado)

        return resultados

    clientes = asesor2(datos)
    print(clientes)





