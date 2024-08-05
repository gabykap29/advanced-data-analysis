from database.db_connection import Session, engine, Base
from models import employee_perfomance
from utils.add_data_to_mysql import add_data_to_mysql

if __name__ == "__main__":
    add_data_to_mysql()
    print("Data added to MySQL")


