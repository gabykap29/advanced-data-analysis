from services.median_logic import MendianLogic
from services.plots import PlotsMathplolib
from services.correlations import FunctionCorrelation
from utils.connection_db import ConnectionDB

class DataAnalysis:
    def __init__(self):
        # Inicialización de las clases responsables de cálculos y gráficos
        self.fc = FunctionCorrelation()
        self.ml = MendianLogic()
        self.plots = PlotsMathplolib()
        self.connection = ConnectionDB()

    # Método que ejecuta el análisis de datos
    def run_analysis(self):
        self.connection.add_data_to_mysql()
        print("Data added to MySQL")

        print("Calculating mean of performance_score")
        self.ml.function_to_calculate_mean()
        print("Calculating median of performance_score")
        self.ml.function_to_calculate_medians()
        print("Calculating std of performance_score")
        self.ml.function_to_calculate_std()
        print("Calculating mean of salary")
        self.ml.function_to_calculate_mean_salary()
        print("Calculating median of salary")
        self.ml.function_to_calculate_medians_salary()
        print("Calculating std of salary")
        self.ml.function_to_calculate_std_salary()
        print("All calculations done")

        print("Calculating correlation between performance_score and salary")
        self.fc.function_correlation_salary()
        self.fc.function_correlation_years()
        print("All calculations done")

        print("Generating graphs")
        self.plots.histograma_performance_score_department()
        self.plots.scatterplot_years_with_company_vs_performance_score()
        self.plots.scatterplot_salary_vs_performance_score()
        print("All graphs done")
# Path: main.py se utiliza en __name__ para ejecutar el análisis de datos si se ejecuta el archivo main.py
if __name__ == "__main__":
    analysis = DataAnalysis()
    analysis.run_analysis()
