from database.db_connection import Session, engine, Base
from models import employee_perfomance
from pandas import pandas as pd
import os

#Funcion para cargar los datos desde un csv a la base de datos con sqlalchemy y pandas

def add_data_to_mysql():
    #Verificamos si la bd esta creada
    Base.metadata.create_all(bind=engine)
    #Abrimos la session
    session = Session()

    #obtenemos la ruta relativa del archivo csv
    path = os.path.join(os.path.dirname(__file__), "data_employes.csv")
    #Leemos el csv
    data = pd.read_csv(path, delimiter=",")
    #Iteramos sobre el dataframe
    for index, row in data.iterrows():
        #Creamos un objeto de la clase EmployeePerfomance
        employee = employee_perfomance.EmployeePerfomance(
            id = row["id"],
            employee_id = row["employee_id"],
            department = row["department"],
            performance_score = row["performance_score"],
            years_with_company = row["years_with_company"],
            salary = row["salary"]
        )
        #Agregamos el objeto a la session
        session.add(employee)
    #Guardamos los cambios
    session.commit()
    #Cerramos la session
    session.close()
