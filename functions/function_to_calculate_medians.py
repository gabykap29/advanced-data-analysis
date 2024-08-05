from pandas import pandas as pd
from functions.load_data_to_pandas import load_data_to_pandas

dataframe = load_data_to_pandas()

#funciones para perfomance_score
def function_to_calculate_mean():
    print(dataframe)
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


#funciones para salary

def function_to_calculate_mean_salary():
    try:
        #calculamos la media de la columna salary
        mean_salary = dataframe["salary"].mean()
        print("La media de la columna salary es: ", mean_salary)
        return mean_salary
    except:
        print("Error al calcular la media de la columna salary")
    return mean_salary

def function_to_calculate_medians_salary():
    try:
        #calculamos la mediana de la columna salary
        median_salary = dataframe["salary"].median()
        print("La mediana de la columna salary es: ", median_salary)
        return median_salary
    except:
        print("Error al calcular la mediana de la columna salary")
    return median_salary

def function_to_calculate_std_salary():
    try:
        #calculamos la desviacion estandar de la columna salary
        std_salary = dataframe["salary"].std()
        print("La desviacion estandar de la columna salary es: ", std_salary)
        return std_salary
    except:
        print("Error al calcular la desviacion estandar de la columna salary")
    return std_salary