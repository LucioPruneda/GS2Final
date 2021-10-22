from tkinter import ttk
from tkinter import *
import sqlite3

class Gastos:
    

    def __init__(self, window):
        # Inicializacion 
        self.wind = window
        self.wind.title('Aplicacion de Gastos')



if __name__ == '__main__':
    window = Tk()
    application = Gastos(window)
    window.mainloop()