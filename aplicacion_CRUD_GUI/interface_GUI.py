import CRUD
import tkinter as tk
from tkinter import *

def ventana_menu_ppal(tareas):
    #Creo la ventana
    m = tk.Tk()
    m.title("App CRUD de tareas")
    m.geometry("800x600")
    
    #Frame de la tabla    
    marcoTabla = Frame(m, borderwidth = 2)
    marcoTabla.config(width = "600", height = "300")
    marcoTabla.config(bg = "#3D985D")
    marcoTabla.grid(row = 0, column = 0, columnspan = 2, rowspan = 2)# Mostrar el Frame
    
    #Frame del CRUD 
    marcoCRUD = Frame(m, borderwidth = 2, relief = "raised")
    marcoCRUD.config(width = "600", height = "300")
    marcoCRUD.config(bg = "#35B963")
    marcoCRUD.grid(row = 2, column = 0) 
    
    #Frame imagen
    marcoImg = Frame(m, borderwidth = 2, relief = "raised")
    marcoImg.config(width = "200", height = "300")
    marcoImg.config(bg = "#2BD265")
    marcoImg.grid(row = 0, column = 2)  
    
    #Frame de los botones
    marcoBotones = Frame(m, borderwidth = 2, relief = "raised")
    marcoBotones.config(width = "200", height = "300")
    marcoBotones.config(bg = "#14F161")
    marcoBotones.grid(row = 2, column = 2)    
    
    return m
