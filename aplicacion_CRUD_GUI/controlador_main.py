import CRUD
import interface_GUI as iGUI
import tkinter as tk
import sys

tareas = CRUD.Read()
if not(tareas):
    sys.exit(1)
    
m = iGUI.ventana_menu_ppal(tareas)

m.mainloop()    

