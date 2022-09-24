# pseudo codigo
# main()
#   datos = get_data(filename)
#   reporte = generate_report(datos)
#   save_date(reporte)

import os
from pathlib import Path
import pandas as pd
root_dir = Path(".").resolve()

def get_data(filename):
    
    data_dir = 'row'
    file_path=os.path.join(root_dir, "data",data_dir, filename)
    datos = pd.read_csv(file_path, encoding="latin-1", sep=':')
    print('get_data')
    print('La tabla contiene', datos.shape[0],'filas',datos.shape[1],'columnas')
    return datos

def generate_report(datos):
    # Crear un diccionadio vacio
    dict_resumen = dict()

    for col in datos.columns:
        valores_unicos = datos[col].unique()
        n_valores = len(valores_unicos)
        dict_resumen[col] = n_valores

    reports = pd.DataFrame.from_dict(dict_resumen, orient='index')
    #report.rename()
    return reports

def save_data(reporte,filename):
    #Guarda la tabla

    out_name = 'resumen' + filename
    out_path = os.path.join(root_dir,'data','processed',out_name)
    reporte.to_csv(out_path)
    reporte

def main ():

    filename="llamadas123_julio_2022.csv"
    datos = get_data(filename)
    reporte = generate_report(datos)
    save_data(reporte,filename)

if __name__ == '__main__':
    main()