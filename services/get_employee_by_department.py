from pandas import pandas as pd
from load_data_to_pandas import load_data_to_pandas

dataframe = load_data_to_pandas()

#funcion para obtener el total de empleados divididos por departamento

def get_employee_by_department():
    try:
        #obtenemos el total de empleados por departamento
        employee_by_department = dataframe["department"].value_counts()
        print("Total de empleados por departamento: \n", employee_by_department)
        return employee_by_department
    except:
        print("Error al obtener el total de empleados por departamento")
    return employee_by_department