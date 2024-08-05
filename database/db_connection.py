from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#conexion a mysql

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/CompanyData" #root:root@localhost:3306

#creamos una base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
#creamos una sesion
Session = sessionmaker(bind=engine)
#creamos una base de datos declarativa
Base= declarative_base()

