from matplotlib import pyplot as plt
import numpy as np
from services.load_data_to_pandas import load_data_to_pandas

#utilizamos mathplotlib para graficar performance_score de cada departamento

class PlotsMathplolib:
    def __init__(self):
        self.dataframe = load_data_to_pandas()

    def histograma_performance_score_department(self):
        data = self.dataframe
        data = data[['department', 'performance_score']]
        data = data.groupby('department').mean()
        data = data.sort_values(by='performance_score', ascending=False)
        data.plot(kind='bar', y='performance_score', color='blue')
        plt.title('Performance Score por Departamento')
        plt.ylabel('Performance Score')
        plt.xlabel('Departamento')
        plt.show()

    #Gráfico de dispersión de years_with_company vs. performance_score.
    def scatterplot_years_with_company_vs_performance_score(self):
        data = self.dataframe
        data = data[['years_with_company', 'performance_score']]
        data.plot(kind='scatter', x='years_with_company', y='performance_score', color='blue')
        plt.title('Years with Company vs Performance Score')
        plt.ylabel('Performance Score')
        plt.xlabel('Years with Company')
        plt.show()


    #Gráfico de dispersión de salary vs. performance_score.
    def scatterplot_salary_vs_performance_score(self):
        data = self.dataframe
        data = data[['salary', 'performance_score']]
        data.plot(kind='scatter', x='salary', y='performance_score', color='blue')
        plt.title('Salary vs Performance Score')
        plt.ylabel('Performance Score')
        plt.xlabel('Salary')
        plt.show()
