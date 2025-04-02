import tkinter as tk
import sqlite3

class App:
    def __init__(self, ventana_principal):        
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Biblioteca")
    
    #base de datos
        self.con = sqlite3.connect('libros.db')
        self.cur = self.con.cursor()
        
        self.cur.execute('CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, año INTEGER)')
        self.con.commit()
        
        self.label_titulo = tk.Label(self.ventana_principal, text = 'Titulo')
        self.label_titulo.pack(pady = 5)
        
        self.entry_titulo = tk.Entry(self.ventana_principal)
        self.entry_titulo.pack(pady = 5)

        self.label_autor = tk.Label(self.ventana_principal, text = 'autor')
        self.label_autor.pack(pady = 5)

        self.entry_autor = tk.Entry(self.ventana_principal)
        self.entry_autor.pack(pady = 5)
        
        self.label_año = tk.Label(self.ventana_principal, text = 'año')
        self.label_año.pack(pady = 5)
        
        self.entry_año = tk.Entry(self.ventana_principal)
        self.entry_año.pack(pady = 5)
        
        self.listbox = tk.Listbox(self.ventana_principal, width=50)
        self.listbox.pack(pady=5)
        
        self.boton_guardar = tk.Button(self.ventana_principal, text = 'guardar', command = self.guardar_datos)
        self.boton_guardar.pack(pady = 20)
        
        self.boton_mostrar = tk.Button(self.ventana_principal, text = 'mostrar', command = self.mostrar_datos)
        self.boton_mostrar.pack(pady = 20)
        
        self.boton_actualizar = tk.Button(self.ventana_principal, text = 'actualizar', command = self.actualizar_datos)
        self.boton_actualizar.pack(pady = 20)

        self.boton_eliminar = tk.Button(self.ventana_principal, text = 'eliminar', command = self.eliminar_datos)
        self.boton_eliminar.pack(pady = 20)
    
    def guardar_datos(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        año = self.entry_año.get()
        
        self.cur.execute('INSERT INTO libros (titulo, autor, año) VALUES (?,?,?)', (titulo, autor, año))
        self.con.commit()
        
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_año.delete(0, tk.END)
    
    def mostrar_datos(self):
        self.listbox.delete(0,tk.END)
        
        self.cur.execute('SELECT * FROM libros')
        registros = self.cur.fetchall()
        
        for registro in registros:
            self.listbox.insert(tk.END, f"ID: {registro[0]}, titulo: {registro[1]}, autor: {registro[2]}, año: {registro[3]}")
    
    def actualizar_datos(self):
        seleccion = self.listbox.curselection()
        
        if seleccion:
            index = seleccion[0]
            registro = self.listbox.get(index)
            registro_id = registro.split(',')[0].split(':')[1]
            
            nuevo_titulo = self.entry_titulo.get()
            nuevo_autor = self.entry_autor.get()
            nuevo_año = self.entry_año.get()
            
            self.cur.execute('UPDATE libros SET titulo = ?, autor = ?, año = ? WHERE id = ?',(nuevo_titulo, nuevo_autor, nuevo_año, registro_id))
            self.con.commit()
            
            self.mostrar_datos()
            
            self.entry_titulo.delete(0,tk.END)
            self.entry_autor.delete(0,tk.END)
            self.entry_año.delete(0,tk.END)
        else:
            print("No hay ningun resigistro seleccionado para actualizar")
    
    def eliminar_datos(self):
        seleccion = self.listbox.curselection()
        
        if seleccion:
            index = seleccion[0]
            registro = self.listbox.get(index)
            registro_id = registro.split(',')[0].split(':')[1]
            
            self.cur.execute('DELETE FROM libros WHERE id = ?',(registro_id,))
            self.con.commit()
            
            self.mostrar_datos()
        else:
            print("No hay ningun resigistro seleccionado para eliminar")

mi_ventana =tk.Tk()
app = App(mi_ventana)
mi_ventana.mainloop()
        