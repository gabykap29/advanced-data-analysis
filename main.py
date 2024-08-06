from database.db_connection import Session, engine, Base
from models import employee_perfomance
from utils.add_data_to_mysql import add_data_to_mysql
from functions.function_to_calculate_medians import * 
from functions.function_correlation import *
from functions.function_to_matplolib import *

if __name__ == "__main__":
    add_data_to_mysql()
    print("Data added to MySQL")
    print("Calculating mean of performance_score")
    function_to_calculate_mean()
    print("Calculating median of performance_score")
    function_to_calculate_medians()
    print("Calculating std of performance_score")
    function_to_calculate_std()
    print("Calculating mean of salary")
    function_to_calculate_mean_salary()
    print("Calculating median of salary")
    function_to_calculate_medians_salary()
    print("Calculating std of salary")
    function_to_calculate_std_salary()
    print("All calculations done")
    #calculamos la correlacion entre performance_score y salary
    print("Calculating correlation between performance_score and salary")
    function_correlation_salary()
    function_correlation_years()
    print("All calculations done")
    #graficamos los datos
    histograma_performance_score_department()
    scatterplot_years_with_company_vs_performance_score()
    scatterplot_salary_vs_performance_score()
    print("All graphs done")



