#Librerias:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # type: ignore
#Seaborn para visualizacion de datos
import seaborn as sns # type: ignore
import os
import io

class DataAnalyzer:
    def __init__(self, data):
        self.df = data

    def summary(self):
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        salida = buffer.getvalue()
        salida_describe = self.df.describe().to_string()
        salida += "\n\n" + salida_describe
        return salida
    
        #print(self.df.describe())

    def missing_values(self):
        return self.df.isnull().sum()

    def imprimir(self):
        print("Hola")

    def correlation_matrix(self):
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        corr = self.df[numeric_cols].corr()
        plt.figure()
        sns.heatmap(corr, annot = True, cmap = 'coolwarm')
        plt.title('Matriz de correlacion')
        plt.show(block=False)

    def categorical_analisis(self):
        categorical_cols = self.df.select_dtypes(include='object').columns
        print(f"Las columnas categóricas son: {categorical_cols}")
        column = input("Digite la columna a visualizar: ")

        if column in categorical_cols:
            plt.figure()
            sns.countplot(data=self.df, x=column, order=self.df[column].value_counts().index)
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("La columna no es categórica o no existe en el dataframe.")
        