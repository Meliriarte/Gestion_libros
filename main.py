import tkinter as tk
from modelo import Modelo
from vista import Vista
from controlador import Controlador

def main():
    root = tk.Tk()
    
    modelo = Modelo()
    vista = Vista(root)
    controlador = Controlador(vista, modelo)
    
    root.mainloop()
    
    # Cerrar la conexión a la base de datos al salir
    modelo.cerrar_conexion()

if __name__ == "__main__":
    main()