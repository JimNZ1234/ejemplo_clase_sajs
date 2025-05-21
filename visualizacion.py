#Librerias:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
#Para visualizacion de datos
import seaborn as sns 
import os
#Para interfaz gráfica completa
import tkinter as tk
#Para importar clases especificas de la libreria
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox, simpledialog, filedialog
#Importar clase
from analisis import DataAnalyzer
#Para imagenes
from PIL import ImageTk

data = pd.read_csv("adult.csv")
df = data.copy()
analizar = DataAnalyzer(data)

def informacion():
    try:
        text_area.delete("1.0",tk.END) #Para vaciar al ejecutar
        info = analizar.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerror("Error","No se puede")

def mostrar_imagenes(pil_img):
    image_tk = ImageTk.PhotoImage(pil_img)
    image_label.configure(image=image_tk)
    image_label.image = image_tk

def mostrar_correlacion():
    img = analizar.correlation_matrix()
    mostrar_imagenes(img)

def mostrar_categorico():
    cols = analizar.df.select_dtypes(include="object").columns.tolist()
    if not cols:
        messagebox.showwarning("Atencion", "El dataframe no tiene columnas categoricas")
    else:
        sel = simpledialog.askstring("Columna" , f"Elige una:\n {cols}")
        if sel in cols:
            img = analizar.categorical_analisis_col(sel)
            mostrar_imagenes(img)

def añadir_usuario():
    
    cols = analizar.df.columns.tolist()
    usuario = {}
    for i in cols:
        añadir = simpledialog.askstring("Añadir info" , f"Digita tu informacion de {i}: ")
        if añadir:
            usuario[i] = añadir
        else:
            messagebox.showwarning("Atencion", "No ingreso nada")

    df.loc[len(df)] = usuario
    df.to_csv("Nuevos_usuarios.csv", index = False)
    print(df.tail())
        

ventana = tk.Tk()
ventana.title("Visualización de los datos")
ventana.geometry()

boton_summary = tk.Button(ventana, text="Resumen", command=informacion)
boton_summary.grid(row=0, column=0)

boton_numerico = tk.Button(ventana, text="Numerico", command=mostrar_correlacion)
boton_numerico.grid(row=0, column=1)

boton_categorico = tk.Button(ventana, text="Categorico", command=mostrar_categorico)
boton_categorico.grid(row=1, column=0)

boton_usuarios = tk.Button(ventana, text="Añadir usuario", command=añadir_usuario)
boton_usuarios.grid(row=2, column=0)

text_area = ScrolledText(ventana, width= 70, height= 30)
text_area.grid(row=1, column=1)

content_frame = tk.Frame(ventana)
content_frame.grid(row=1, column=2)

image_label = tk.Label(content_frame, text="Resultado")
image_label.grid(row=0, column=0)

ventana.mainloop()

#analizar.correlation_matrix()
#analizar.categorical_analisis