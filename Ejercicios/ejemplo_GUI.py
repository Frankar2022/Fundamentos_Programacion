import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Mi primera ventana")
boton_1 = ttk.Button(ventana, text="Click aquí Hola Mundo")
boton_1.pack()
ventana.mainloop()
