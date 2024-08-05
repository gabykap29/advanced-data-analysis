from sqlalchemy import Column, Integer, String, Float
from database.db_connection import Base

#creamos una clase que hereda de Base

class EmployeePerfomance(Base):
    __tablename__ = "employee_perfomance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    department = Column(String(255))
    performance_score = Column(Float)
    years_with_company = Column(Integer)
    salary = Column(Float)



"""
modelo
id (Clave primaria autoincremental)
employee_id (Números enteros)
department (Textos)
performance_score (Números con decimales)
years_with_company (Números enteros)
salary (Números con decimales)

"""