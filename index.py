from tkinter import ttk
from tkinter import *
import sqlite3

class Gastos:
    
    db_name = 'database.db'
    def __init__(self, window):
        # Inicializacion 
        self.bd = sqlite3.connect("bd.sqlite")
        self.cursor = self.bd.cursor()
        self.wind = window
        self.wind.title('Aplicacion de Gastos')


        # Frame 
        frame = LabelFrame(self.wind, text = 'Registra un nuevo gasto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Label motivo
        Label(frame, text = 'Motivo: ').grid(row = 1, column = 0)
        self.motivo = Entry(frame)
        self.motivo.focus()
        self.motivo.grid(row = 1, column = 1)

        # Label precio
        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.precio = Entry(frame)
        self.precio.grid(row = 2, column = 1)

        # Button agrega gasto
        ttk.Button(frame, text = 'Guardar gasto', command = self.add_gasto).grid(row = 3, columnspan = 2, sticky = W + E)

        # Output mensajes 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Tabla
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Motivo', anchor = CENTER)
        self.tree.heading('#1', text = 'Precio', anchor = CENTER)

         # Botones
        ttk.Button(text = 'BORRAR', command = self.delete_gasto).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'EDITAR', command = self.edit_gasto).grid(row = 5, column = 1, sticky = W + E)

        

        # Ejecuta query
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

        # Trae todo
    def get_all(self):
        # Limpiando tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Consultando datos
        query = 'SELECT * FROM gastos'
        db_rows = self.run_query(query)
        # 
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    def validation(self):
        return len(self.motivo.get()) != 0 and len(self.precio.get()) != 0

    def add_gasto(self):
        if self.validation():
            query = 'INSERT INTO gastos VALUES(NULL, ?, ?)'
            parameters =  (self.motivo.get(), self.precio.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Gasto {} agregado correctamente'.format(self.motivo.get())
            self.motivo.delete(0, END)
            self.precio.delete(0, END)
        else:
            self.message['text'] = 'Motivo y precio requerido'
        self.get_all()

    def delete_gasto(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Selecciona un gasto'
            return
        self.message['text'] = ''
        motivo = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM gastos WHERE motivo = ?'
        self.run_query(query, (motivo, ))
        self.message['text'] = '{} borrado correctamente'.format(motivo)
        self.get_all()


    def edit_gasto(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Selecciona un gasto'
            return
        motivo = self.tree.item(self.tree.selection())['text']
        old_precio = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar motivo'
        # Motivo anterior
        Label(self.edit_wind, text = 'Motivo anterior:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = motivo), state = 'readonly').grid(row = 0, column = 2)
        
        # Nuevo motivo
        Label(self.edit_wind, text = 'Motivo nuevo:').grid(row = 1, column = 1)
        new_motivo = Entry(self.edit_wind)
        new_motivo.grid(row = 1, column = 2)

        # Precio anterior
        Label(self.edit_wind, text = 'Precio anterior:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_precio), state = 'readonly').grid(row = 2, column = 2)
        
        # Nuevo precio
        Label(self.edit_wind, text = 'Nuevo precio:').grid(row = 3, column = 1)
        new_precio= Entry(self.edit_wind)
        new_precio.grid(row = 3, column = 2)

        Button(self.edit_wind, text = 'CONFIRMAR', command = lambda: self.edit_records(new_motivo.get(), motivo, new_precio.get(), old_precio)).grid(row = 4, column = 2, sticky = W)
        self.edit_wind.mainloop()

    def edit_records(self, new_motivo, motivo, new_precio, old_precio):
        query = 'UPDATE gastos SET motivo = ?, precio = ? WHERE motivo = ? AND precio = ?'
        parameters = (new_motivo, new_motivo, motivo, old_precio)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = '{} Editado correctamente'.format(motivo)
        self.get_all()




if __name__ == '__main__':
    window = Tk()
    application = Gastos(window)
    window.mainloop()