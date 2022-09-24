import numpy as np
import argparse

def calcular_valores_centrales(lista_numeros, verbose=1):
    """calcula el valor de la media y desviacion estandar de una lista de numeros
    Args:
        lista_numeros(lista): lista de numeros con valores enteros
    return:
        tuple:(media,desviacion_estandar)
    """
    media=np.mean(lista_numeros)
    dev_std=np.std(lista_numeros)
    if verbose ==1:
        print('calcular_valores_centrales')
        print('media',media)
        print('desv std',dev_std)
    else:
        pass
    return media,dev_std

def calcular_suma(lista_numeros,verbose=1):       #Definir lista de la suma
    '''
    calcular la suma de una lista de numeros
    Args:
        lista_numeros : lista de numeros
    '''
    resultado = np.sum(lista_numeros)   #Libreria numpy para suma de funcion
    if verbose ==1:
        print('calcular_suma')
        print('suma:',resultado)
    else:
        pass
    return resultado

def calcular_extremos (lista_numeros,verbose=1):
    """calcula el valor minimo y maximo de una lista de numeros
    Args:
        lista_numeros(lista): lista de numeros con valores enteros
    return:
        tuple:(minimo,maximo)
    """
    min_val=np.min(lista_numeros)
    max_val=np.max(lista_numeros)
    if verbose ==1:
        print('calcular_extremos')
        print('min:',min_val)
        print('max:',max_val)
    else:
        pass
    return min_val, max_val

def calcular_valores(lista_numeros,verbose=1):    #Definir la funcion no olvidar dos puntos al final
    
    suma = calcular_suma(lista_numeros,verbose)
    media, dev_std = calcular_valores_centrales(lista_numeros,verbose)
    min_val,max_val = calcular_extremos(lista_numeros,verbose)
    return suma, media, dev_std, min_val,max_val

def main():
    parser = argparse.ArgumentParser() 
    parser.add_argument("--verbose",type=int,default=1,help="para decidir si imprime informacion")
    args = parser.parse_args()
    verbose = args.verbose
    lista_numeros = [1,5,8,3,45,93]
    suma, media, dev_std, min_val,max_val = calcular_valores(lista_numeros,verbose)
    print ('DONE!!!')

if __name__ == '__main__':
    main()