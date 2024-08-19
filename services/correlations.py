from pandas import pandas as pd

from services.load_data_to_pandas import load_data_to_pandas

class FunctionCorrelation:
    def __init__(self):
        self.dataframe =  load_data_to_pandas()

    def function_correlation_years(self):
        try:
            # correlación entre years_with_company y performance_score
            correlation = self.dataframe["years_with_company"].corr(self.dataframe["performance_score"])
            print("La correlación entre years_with_company y performance_score es: ", correlation)
            return correlation
        except Exception as e:
            print(f"Error al calcular la correlación entre years_with_company y performance_score: {e}")
            return None

    def function_correlation_salary(self):
        try:
            # Calculamos la correlación entre salary y performance_score
            correlation_salary = self.dataframe["salary"].corr(self.dataframe["performance_score"])
            print("La correlación entre salary y performance_score es: ", correlation_salary)
            return correlation_salary
        except Exception as e:
            print(f"Error al calcular la correlación entre salary y performance_score: {e}")
            return None
