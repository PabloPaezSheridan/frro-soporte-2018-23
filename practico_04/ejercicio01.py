# 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
# Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
# al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2. 

import tkinter

def calcular(operacion):
    if not tBVariable1.get() or not tBVariable2.get():
        print("Complete los campos")
    else:
        text = tBVariable1.get() + operacion + tBVariable2.get()
        print(eval(text))


ventana = tkinter.Tk()


# Estiquetas
etiqueta1 = tkinter.Label(ventana, text="Primer operando")
etiqueta2 = tkinter.Label(ventana, text="Segundo operando")

# Estiquetas en pantalla
etiqueta1.grid(row=0, column=0, padx=5, pady=5)
etiqueta2.grid(row=0, column=1, padx=5, pady=5)

# Entrada
tBVariable1 = tkinter.Entry(ventana)
tBVariable2 = tkinter.Entry(ventana)

# Entrada en pantalla
tBVariable1.grid(row=1, column=0, padx=5, pady=5)
tBVariable2.grid(row=1, column=1, padx=5, pady=5)


# Botones
btnSuma = tkinter.Button(ventana, text="+", width=2, heigh=1, command=lambda: calcular("+"))
btnResta = tkinter.Button(ventana, text="-", width=2, heigh=1, command=lambda: calcular("-"))
btnPor = tkinter.Button(ventana, text="x", width=2, heigh=1, command=lambda: calcular("*"))
btnDiv = tkinter.Button(ventana, text="%", width=2, heigh=1, command=lambda: calcular("/"))

# Botones en pantalla
btnSuma.grid(row=1, column=2, padx=5, pady=5)
btnResta.grid(row=1, column=3, padx=5, pady=5)
btnPor.grid(row=1, column=4, padx=5, pady=5)
btnDiv.grid(row=1, column=5, padx=5, pady=5)


ventana.mainloop()
