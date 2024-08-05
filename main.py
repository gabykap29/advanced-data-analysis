from .database.db_connection import Session, engine, Base
from .models import employee_perfomance

if __name__ == "__main__":
    #creamos la base de datos
    Base.metadata.create_all(bind=engine)

    #Abro la session
    session = Session()

    