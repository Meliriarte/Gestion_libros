import tkinter as tk

class Vista:
    def __init__(self, master):
        self.master = master
        self.master.title("Biblioteca")
        
        self.label_titulo = tk.Label(master, text='Título')
        self.label_titulo.pack(pady=5)
        self.entry_titulo = tk.Entry(master)
        self.entry_titulo.pack(pady=5)

        self.label_autor = tk.Label(master, text='Autor')
        self.label_autor.pack(pady=5)
        self.entry_autor = tk.Entry(master)
        self.entry_autor.pack(pady=5)
        
        self.label_año = tk.Label(master, text='Año')
        self.label_año.pack(pady=5)
        self.entry_año = tk.Entry(master)
        self.entry_año.pack(pady=5)
        
        self.listbox = tk.Listbox(master, width=50)
        self.listbox.pack(pady=5)
        
        self.boton_guardar = tk.Button(master, text='Guardar')
        self.boton_guardar.pack(pady=5)
        
        self.boton_mostrar = tk.Button(master, text='Mostrar')
        self.boton_mostrar.pack(pady=5)
        
        self.boton_actualizar = tk.Button(master, text='Actualizar')
        self.boton_actualizar.pack(pady=5)

        self.boton_eliminar = tk.Button(master, text='Eliminar')
        self.boton_eliminar.pack(pady=5)
    
    def obtener_datos_entrada(self):
        return {
            'titulo': self.entry_titulo.get(),
            'autor': self.entry_autor.get(),
            'año': self.entry_año.get()
        }
    
    def limpiar_entradas(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_año.delete(0, tk.END)
    
    def mostrar_libros(self, libros):
        self.listbox.delete(0, tk.END)
        for libro in libros:
            self.listbox.insert(tk.END, f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Año: {libro[3]}")
    
    def obtener_seleccion(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            return self.listbox.get(seleccion[0])
        return None
    
    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")  