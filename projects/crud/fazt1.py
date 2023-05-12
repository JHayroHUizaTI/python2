from tkinter import ttk
from tkinter import *
import sqlite3 

class Producto:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Productos')

        # Crear un contenedor
        frame = LabelFrame(self.wind, text = 'Registrar Producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Nombre de producto
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Descripcion
        Label(frame, text = 'Descripcion: ').grid(row = 2, column = 0)
        self.description = Entry(frame)
        self.description.grid(row = 2, column = 1)

        # Precio
        Label(frame, text = 'Precio: ').grid(row = 3, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 3, column = 1)

        #button add product
        ttk.Button(frame, text = 'save product').grid(row = 4, columnspan = 2, sticky = W + E)


        #table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 5, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Price', anchor = CENTER)

        # Output message

if __name__ == "__main__":
    window = Tk()
    application = Producto(window)
    window.mainloop()