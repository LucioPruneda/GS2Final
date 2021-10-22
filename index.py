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

        # Label
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)




if __name__ == '__main__':
    window = Tk()
    application = Gastos(window)
    window.mainloop()