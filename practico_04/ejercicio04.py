# 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
# que inicia otra venta donde puedo ingresar una ciudad y su código postal .
# 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
# 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 

import tkinter as tk
from tkinter import ttk
from tkinter import *
from ejercicio03 import TreeCiudades


class City:

    def __init__(self, citysDesktop):
        self.citysDesktop = citysDesktop
        self.citysDesktop.title("Ciudades")

    def citys(self):
        btnNewCity = tk.Button(citysWindow, text="Agregar", command=self.newCity)
        btnNewCity.grid(row=0)
        btnNewCity.pack()

        btnDelete = tk.Button(citysWindow, text="Eliminar", command=self.deleteCity)
        btnDelete.pack()

        btnModificar = tk.Button(citysWindow, text="Modificar", command=self.modifyCity)
        btnModificar.pack()

        self.trv = TreeCiudades(self.citysDesktop)
        self.trv.pack()

    def newCity(self):
        new = tk.Toplevel(citysWindow)

        frame = LabelFrame(new, text="Ingresar Nueva Ciudad")
        frame.grid(row=0, column=0, columnspan=2, pady=20)

        lblCity = ttk.Label(frame, text="Ciudad: ")
        lblCity.grid(column=0, row=1)

        self.city = tk.StringVar()
        self.txtCity = ttk.Entry(frame, width=15, textvariable=self.city)
        self.txtCity.focus()
        self.txtCity.grid(column=1, row=1)

        lblPC = ttk.Label(frame, text="Codigo Postal: ")
        lblPC.grid(column=0, row=2)

        self.pc = tk.StringVar()
        self.txtPC = ttk.Entry(frame, width=15, textvariable=self.pc)
        self.txtPC.grid(column=1, row=2)

        btnSave = ttk.Button(frame, text="Guardar Ciudad", command=self.addCity)
        btnSave.grid(column=1, row=3, columnspan=2)

    def addCity(self):
        self.trv.insert("", "end", text=self.city.get(), values=(self.pc.get()))
        self.txtCity.delete(0, END)
        self.txtPC.delete(0, END)

    def deleteCity(self):
        item = self.trv.selection()
        self.trv.delete(item)

    def modifyCity(self):
        try:
            self.trv.item(self.trv.selection())['text'][0]
        except IndexError as e:
            # mostrar error
            return

        new = tk.Toplevel(citysWindow)

        frame = LabelFrame(new, text="Modifica una ciudad")
        frame.grid(row=0, column=0, columnspan=2, pady=20)

        curItem = self.trv.item(self.trv.selection())

        lblCity = ttk.Label(frame, text="Nombre viejo")
        lblCity.grid(column=0, row=1)

        lblCity = ttk.Label(frame, text=curItem["text"])
        lblCity.grid(column=1, row=1)

        lblCity = ttk.Label(frame, text="Nombre nuevo: ")
        lblCity.grid(column=0, row=2)

        self.city = tk.StringVar()
        self.txtCity = ttk.Entry(frame, width=15, textvariable=self.city)
        self.txtCity.focus()
        self.txtCity.grid(column=1, row=2)

        lblPC = ttk.Label(frame, text="Codigo Postal Viejo: ")
        lblPC.grid(column=0, row=3)

        lblPC = ttk.Label(frame, text=curItem["values"])
        lblPC.grid(column=1, row=3)

        lblPC = ttk.Label(frame, text="Codigo Postal Nuevo: ")
        lblPC.grid(column=0, row=4)

        self.pc = tk.StringVar()
        self.txtPC = ttk.Entry(frame, width=15, textvariable=self.pc)
        self.txtPC.grid(column=1, row=4)

        btnSave = ttk.Button(frame, text="Guardar Ciudad", command=self.updateCity)
        btnSave.grid(column=1, row=5, columnspan=2)

    def updateCity(self):
        self.trv.item(self.trv.selection(), text=self.city.get(), values=(self.pc.get()))
        self.txtCity.delete(0, END)
        self.txtPC.delete(0, END)


if __name__ == '__main__':
    citysWindow = Tk()
    application = City(citysWindow)
    application.citys()
    citysWindow.mainloop()
