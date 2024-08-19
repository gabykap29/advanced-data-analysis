from database.db_connection import Session, engine, Base
from models import employee_perfomance
from pandas import pandas as pd
import os

# Función para cargar los datos desde un csv a la base de datos con sqlalchemy y pandas
class ConnectionDB:
    def __init__(self):
        pass
    def add_data_to_mysql(self):
        try:
            # Verificamos si la bd está creada
            Base.metadata.create_all(bind=engine)
            # Abrimos la sesión
            session = Session()
            # Obtenemos la ruta relativa del archivo csv
            #Verficamos que no haya datos en la tabla
            session.query(employee_perfomance.EmployeePerfomance).delete()
            session.commit()
            path = os.path.join(os.path.dirname(__file__), "data_employes.csv")
            # Leemos el csv
            data = pd.read_csv(path, delimiter=",")

            # Imprimir los nombres de las columnas para verificar
            print("Columnas del DataFrame:", data.columns)


            # Iteramos sobre el DataFrame
            for index, row in data.iterrows():
                # Creamos un objeto de la clase EmployeePerformance
                employee = employee_perfomance.EmployeePerfomance(
                    id=row["id"],
                    employee_id=row["employee_id"],
                    department=row["department"],
                    performance_score=row["performance_score"],
                    years_with_company=row["years_with_company"],
                    salary=row["salary"]
                )
                # Agregamos el objeto a la sesión
                session.add(employee)

            # Guardamos los cambios
            session.commit()
            # Cerramos la sesión
            session.close()
            print("Data added to MySQL")
            return True

        except Exception as e:
            print("Error al agregar los datos a MySQL:", str(e))
            return False
