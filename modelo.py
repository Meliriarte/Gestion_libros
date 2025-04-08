import sqlite3

class Modelo:
    def __init__(self):
        self.con = sqlite3.connect('libros.db')
        self.cur = self.con.cursor()
        self.crear_tabla()
    
    def crear_tabla(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS libros 
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                         titulo TEXT, autor TEXT, año INTEGER)''')
        self.con.commit()
    
    def guardar_libro(self, titulo, autor, año):
        self.cur.execute('INSERT INTO libros (titulo, autor, año) VALUES (?,?,?)', 
                        (titulo, autor, año))
        self.con.commit()
    
    def obtener_libros(self):
        self.cur.execute('SELECT * FROM libros')
        return self.cur.fetchall()
    
    def actualizar_libro(self, libro_id, nuevo_titulo, nuevo_autor, nuevo_año):
        self.cur.execute('''UPDATE libros SET titulo=?, autor=?, año=? 
                          WHERE id=?''', 
                        (nuevo_titulo, nuevo_autor, nuevo_año, libro_id))
        self.con.commit()
    
    def eliminar_libro(self, libro_id):
        self.cur.execute('DELETE FROM libros WHERE id=?', (libro_id,))
        self.con.commit()
    
    def cerrar_conexion(self):
        self.con.close()