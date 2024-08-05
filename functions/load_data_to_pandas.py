from pandas import pandas as pd
from database.db_connection import Session, engine, Base
from models import employee_perfomance
import os

#funcion para obtener todos los datos desde mysql a un dataframe
def load_data_to_pandas():
    #Abrimos la session
    session = Session()
    #Obtenemos todos los datos de la tabla
    data = session.query(employee_perfomance.EmployeePerfomance).all()
    #Cerramos la session
    session.close()
    #Creamos un diccionario con los datos
    data_dict = {}
    data_dict["id"] = []
    data_dict["employee_id"] = []
    data_dict["department"] = []
    data_dict["performance_score"] = []
    data_dict["years_with_company"] = []
    data_dict["salary"] = []
    #Iteramos sobre los datos y los agregamos al diccionario
    for employee in data:
        data_dict["id"].append(employee.id)
        data_dict["employee_id"].append(employee.employee_id)
        data_dict["department"].append(employee.department)
        data_dict["performance_score"].append(employee.performance_score)
        data_dict["years_with_company"].append(employee.years_with_company)
        data_dict["salary"].append(employee.salary)
    #Creamos un dataframe con los datos
    df = pd.DataFrame(data_dict)
    return df
