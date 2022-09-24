# PSEUDOCODIGO
# main()
# cargar archivos - leer datos; recibe el nombre del archivo en un string
# limpieza filas duplicados
# limpieza de nulos
# edad formato bueno esta en string y estamos esperando un numero
# corregir fechas
# guardar
# main ()
#   datos = leer_datos (nombre del archivo : str)  --> pd.dataframe
#   datos = remover_duplicados_y_nulos (datos: pd.dataframe)  --> pd-datfr revisar los indices
#   datos = convertir_str_a_num(datos, col ='EDAD')  --> pd.dataframe  limpieza exclusiva para una columna
#   datos = corregir_fechas(datos, col='FECHA1') --> pd.dataframe
#   datos = corregir_fechas(datos, col='FECHA2') --> pd.dataframe
#   save_data()

from turtle import clear
import numpy as np
import pandas as pd
import os
from pathlib import Path

root_dir = Path(".").resolve()

def get_data(filename):
    
    data_dir = 'row'
    file_path=os.path.join(root_dir, "data",data_dir, filename)
    data = pd.read_csv(file_path, encoding="latin-1", sep=':')
    print('get_data')
    print('La tabla contiene', data.shape[0],'filas',data.shape[1],'columnas')
    return data

def duplicados(data):

    data=data.drop_duplicates()
    data.reset_index(inplace=True, drop=True)


def col = 'UNIDAD':
    data [col].fillna('SIN_DATO',inplace=True)
    data[col].value_counts(dropna=False, normalize=True)

def main ():

    filename="llamadas123_julio_2022.csv"
    data = get_data(filename)
   

if __name__ == '__main__':
    main()