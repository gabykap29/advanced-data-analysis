from pandas import pandas as pd
from load_data_to_pandas import load_data_to_pandas

dataframe = load_data_to_pandas()
def function_to_calculate_mean():
    try:
         #calculamos la media de la columna performance_score
        mean_performance_score = dataframe["performance_score"].mean() 
        print("La media de la columna performance_score es: ", mean_performance_score)
        return mean_performance_score
    except:
        print("Error al calcular la media de la columna performance_score")
    return mean_performance_score

def function_to_calculate_medians():
    try:
         #calculamos la mediana de la columna performance_score
        median_performance_score = dataframe["performance_score"].median()
        print("La mediana de la columna performance_score es: ", median_performance_score)
        return median_performance_score
    except:
        print("Error al calcular la mediana de la columna performance_score")
    return median_performance_score

def function_to_calculate_std():
        try:
            #calculamos la desviacion estandar de la columna performance_score
            std_performance_score = dataframe["performance_score"].std()
            print("La desviacion estandar de la columna performance_score es: ", std_performance_score)
            return std_performance_score
        except:
            print("Error al calcular la desviacion estandar de la columna performance_score")
    