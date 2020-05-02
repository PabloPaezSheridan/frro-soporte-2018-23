# 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
# Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ). 

import tkinter as tk
from tkinter import ttk



def crearTreeView (main_window):
    
    trv = ttk.Treeview(main_window)

    trv["columns"]=("one")
    trv.column("#0", width=270, minwidth=270, stretch=tk.NO)
    trv.column("one", width=150, minwidth=150, stretch=tk.NO)

    trv.heading("#0",text="Ciudades",anchor=tk.W)
    trv.heading("one", text="Codigo Postal",anchor=tk.W)

    trv.insert("", "end", text="Buenos Aires", values=("1675"))
    trv.insert("", "end", text="Rosario", values=("2000"))
    trv.insert("", "end", text="Mendoza", values=("5500"))
    trv.insert("", "end", text="Cordoba", values=("5000"))
    trv.insert("", "end", text="Tucuman", values=("4000"))
    
    trv.pack()
    return trv

main_window = tk.Tk()
main_window.title("Vista de árbol en Tkinter")
crearTreeView(main_window)
main_window.mainloop()
