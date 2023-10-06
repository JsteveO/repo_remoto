#reader es un iterable
#'next sirve para iterar manualemente por lo tanto solo llama la primera fila
#se debe unir los 2 arrays leer y encabezado
import csv

def read_csv(ubi):
  with open(ubi,'r') as filas:
    leer = csv.reader(filas,delimiter=',')
    encabezado = next(leer)
    datos = []
    
    for i in leer:
      unir = zip(encabezado,i,)
      dict = {key: value for key, value in unir}
      datos.append(dict)
      
    return datos
      
if __name__ == '__main__':
  data = read_csv('./proyecto_int/Proyecto_csv.csv')
  print(data)