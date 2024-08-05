from pandas import pandas as pd

from functions.load_data_to_pandas import load_data_to_pandas

dataframe = load_data_to_pandas()

#funcion para obtner la correlacion entre years_with_company y performance_score

def function_correlation_years():
    try:
        #calculamos la correlacion entre years_with_company y performance_score
        correlation = dataframe["years_with_company"].corr(dataframe["performance_score"])
        print("La correlacion entre years_with_company y performance_score es: ", correlation)
        return correlation
    except:
        print("Error al calcular la correlacion entre years_with_company y performance_score")
    return correlation

#funcion  para obtener correlacion entre salary y performance_score
def function_correlation_salary():
    try:
        #calculamos la correlacion entre salary y performance_score
        correlation_salary = dataframe["salary"].corr(dataframe["performance_score"])
        print("La correlacion entre salary y performance_score es: ", correlation_salary)
        return correlation_salary
    except:
        print("Error al calcular la correlacion entre salary y performance_score")
    return correlation_salary