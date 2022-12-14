# PSEUDOCODIGO
# main()
# cargar archivos - leer datos; recibe el nombre del archivo en un string
# limpieza filas duplicados
# limpieza de nulos
# edad formato bueno esta en string y estamos esperando un numero
# corregir fechas
# guardar
# main ()
#   data = get_data (nombre del archivo : str)  --> pd.dataframe
#   data = remover_duplicados_y_nulos (datos: pd.dataframe)  --> pd-datfr revisar los indices
#   data = convertir_str_a_num(datas, col ='EDAD')  --> pd.dataframe  limpieza exclusiva para una columna
#   data = corregir_fechas(data, col='FECHA1') --> pd.dataframe
#   data = corregir_fechas(data, col='FECHA2') --> pd.dataframe
#   save_data()

from turtle import clear
import numpy as np
import pandas as pd
import os
from pathlib import Path
from dateutil.parser import parse

#root_dir = Path(".").resolve()
bucket = 'gs://mdiaz_llamadas_123'

def get_data(filename):
    
    data_dir = 'row'

    file_path=os.path.join(bucket, "data",data_dir, filename)
    data = pd.read_csv(file_path, encoding="latin-1", sep=';')
    return data

def  remover_duplicados_y_nulos(data):

    print ('forma inicial',data.shape)
    data=data.drop_duplicates()
    data.reset_index(inplace=True, drop=True) 
    print ('forma final',data.shape)
    col = 'UNIDAD'
    data[col].fillna('SIN_DATO', inplace= True)
    data[col].value_counts(dropna=False, normalize=True)
    return data

def convertir_str_a_num(data, col ='EDAD'):

    data[col].replace({'SIN_DATO': np.nan}, inplace=True)
    f = lambda x:x if pd.isna(x) else int(x)
    data[col]=data[col].apply(f)
    data[col]
    return data

def corregir_fecha(data, col='FECHA1'):

    
    data[col] = pd.to_datetime(data[col], errors='coerce')
    return data

def corregir_fechas(data, col='FECHA2'):

    list_fechas = list()
    for fecha in data[col]:
        try:
            new_fecha=parse(fecha)
        except Exception as e:
            new_fecha = pd.to_datetime(fecha, errors='coerce')
        list_fechas.append(new_fecha) # A la lista vacia agregarle la nueva fecha
    data['RECEPCION_corr'] = list_fechas
    #data [col] = pd.to_datetime(fecha, errors='coerce')
    data [col] = pd.to_datetime(data[col],errors='coerce')
    return data

def save_data(data,filename):

    out_name = 'limpieza ' + filename
    out_path = os.path.join(bucket,'data','processed',out_name)
    data.to_csv(out_path)
    data

    
def main ():
    
    filename= ["llamadas123_julio_2022.csv", "llamadas123_agosto_2022.csv","llamadas123_junio_2022.csv","datos_llamadas123_mayo_2022.csv","datos_abiertos_enero_2022.csv","datos_abiertos_febrero_2022.csv","datos_abiertos_marzo_2022.csv","datos_abiertos_abril_2022.csv","llamadas_123_abril2021.csv","llamadas_123_agosto2021.csv","llamadas_123_-enero2021.csv","llamadas_123_febrero2021.csv","llamadas_123_julio2021.csv","llamadas_123_marzo2021.csv","llamadas_123_mayo2021.csv","llamadas_123_noviembre_2021.csv","llamadas_123_octubre_2021.csv","llamadas_123_septiembre2021.csv","llamadas123_agosto_2022.csv","llamadas123_junio_2022.csv"]
    dataframe = []
    for filename in filename:
        data = get_data(filename)
        data = remover_duplicados_y_nulos(data)
        data = convertir_str_a_num(data, col ='EDAD')
        data = corregir_fecha(data, col='FECHA_INICIO_DESPLAZAMIENTO_MOVIL')
      #  data = corregir_fechas(data, col='RECEPCION') 
        dataframe.append(data)
    print ('dataframe', dataframe)
    total_datos = pd.concat(dataframe)
    total_datos['CODIGO_LOCALIDAD'] = total_datos['CODIGO_LOCALIDAD'].apply(str)
    save_data(total_datos,'datos_consolidados.csv')

if __name__ == '__main__':
    main()