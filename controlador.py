class Controlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.vista.boton_guardar.config(command=self.guardar_libro)
        self.vista.boton_mostrar.config(command=self.mostrar_libros)
        self.vista.boton_actualizar.config(command=self.actualizar_libro)
        self.vista.boton_eliminar.config(command=self.eliminar_libro)
    
    def guardar_libro(self):
        datos = self.vista.obtener_datos_entrada()
        if datos['titulo'] and datos['autor'] and datos['año']:
            self.modelo.guardar_libro(datos['titulo'], datos['autor'], datos['año'])
            self.vista.limpiar_entradas()
        else:
            self.vista.mostrar_error("Todos los campos son obligatorios")
    
    def mostrar_libros(self):
        libros = self.modelo.obtener_libros()
        self.vista.mostrar_libros(libros)
    
    def actualizar_libro(self):
        seleccion = self.vista.obtener_seleccion()
        if seleccion:
            libro_id = seleccion.split(',')[0].split(':')[1].strip()
            datos = self.vista.obtener_datos_entrada()
            
            if datos['titulo'] and datos['autor'] and datos['año']:
                self.modelo.actualizar_libro(libro_id, datos['titulo'], datos['autor'], datos['año'])
                self.vista.limpiar_entradas()
                self.mostrar_libros()
            else:
                self.vista.mostrar_error("Todos los campos son obligatorios")
        else:
            self.vista.mostrar_error("No hay ningún registro seleccionado para actualizar")
    
    def eliminar_libro(self):
        seleccion = self.vista.obtener_seleccion()
        if seleccion:
            libro_id = seleccion.split(',')[0].split(':')[1].strip()
            self.modelo.eliminar_libro(libro_id)
            self.mostrar_libros()
        else:
            self.vista.mostrar_error("No hay ningún registro seleccionado para eliminar")