#Librerias:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Seaborn para visualizacion de datos
import seaborn as sns
import os
from analisis import DataAnalyzer

data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)

analizar.summary()
analizar.correlation_matrix()
analizar.categorical_analisis