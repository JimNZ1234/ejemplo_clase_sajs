#Librerias:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # type: ignore
#Para visualizacion de datos
import seaborn as sns # type: ignore
import os
#Para interfaz gráfica completa
import tkinter as tk
#Para importar clases especificas de la libreria
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
#Importar clase
from analisis import DataAnalyzer

data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)

def informacion():
    try:
        text_area.delete("1.0",tk.END) #Para vaciar al ejecutar
        info = analizar.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerror("Error","No se puede")

ventana = tk.Tk()
ventana.title("Visualización de los datos")

boton_summary = tk.Button(ventana, text="Info", command=informacion)
boton_summary.pack()

text_area = ScrolledText(ventana, width= 70, height= 30)
text_area.pack()

ventana.mainloop()

#analizar.correlation_matrix()
#analizar.categorical_analisis