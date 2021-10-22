from tkinter import ttk
from tkinter import *
import sqlite3

class Gastos:
    

    def __init__(self, window):
        # Inicializacion 
        self.wind = window
        self.wind.title('Aplicacion de Gastos')


        # Frame 
        frame = LabelFrame(self.wind, text = 'Registra un nuevo gasto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Label motivo
        Label(frame, text = 'Motivo: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Label precio
        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        # Button agrega gasto
        ttk.Button(frame, text = 'Guardar gasto').grid(row = 3, columnspan = 2, sticky = W + E)

        # Tabla
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Motivo', anchor = CENTER)
        self.tree.heading('#1', text = 'Precio', anchor = CENTER)

        





if __name__ == '__main__':
    window = Tk()
    application = Gastos(window)
    window.mainloop()