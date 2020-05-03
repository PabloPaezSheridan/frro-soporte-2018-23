# 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
# que inicia otra venta donde puedo ingresar una ciudad y su código postal .
# 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
# 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 

import tkinter as tk
from tkinter import ttk
from tkinter import *
from ejercicio03 import TreeCiudades

class City:

    def __init__(self,citysDesktop):
        self.citysDesktop= citysDesktop
        self.citysDesktop.title("Ciudades")

    def citys(self):
        btnAlta = tk.Button(citysWindow, text="Alta Ciudad", command=self.newCity)
        btnAlta.pack()
        self.trv = TreeCiudades(citysWindow)
        self.trv.pack()

    def newCity(self):
        new = tk.Toplevel(citysWindow)

        frame = LabelFrame(new, text="Ingresar Nueva Ciudad")
        frame.grid(row = 0, column = 0, columnspan = 2, pady = 20 )
    
        lblCity = ttk.Label(frame, text = "Ciudad: ")
        lblCity.grid(column = 0, row = 1)
    
        self.city = tk.StringVar()
        txtCity = ttk.Entry(frame, width = 15, textvariable = self.city)
        txtCity.focus()
        txtCity.grid(column = 1, row = 1)

        lblPC = ttk.Label(frame, text = "Codigo Postal: ")
        lblPC.grid(column = 0, row = 2)
    
        self.pc= tk.StringVar()
        txtPC = ttk.Entry(frame, width = 15, textvariable = self.pc)
        txtPC.grid(column = 1, row = 2)

        btnSave= ttk.Button(frame, text="Guardar Ciudad", command=self.addCity)
        btnSave.grid(column = 1, row = 3, columnspan = 2)
        
    def addCity(self):
        self.trv.insert("", "end", text=self.city.get(), values=(self.pc.get()))
        
if __name__== '__main__':
    citysWindow = Tk()
    application = City(citysWindow)
    application.citys()
    citysWindow.mainloop()
    