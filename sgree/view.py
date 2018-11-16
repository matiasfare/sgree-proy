#Todo lo que sea Vista
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import model
#Resolucion y pocicion de Ventana Principal
#Principal
resol_poc_vp='700x500+40+20'
#Secundaria
resol_pc_vs='600x300+40+20'
TITULO = 'SGREE'


class VistaPrincipal(tk.PanedWindow, add_recibo):
    '''Vista que contiene pantalla princial, y las llamadas a las funciones'''
    def __init__ (self):
        self.raiz = tk.Tk()
        self.raiz.geometry(resol_poc_vp)
        self.raiz.resizable(width = False, height = False)
        self.raiz.title('Ver Info')
        self.incializar()

    
    def ver_info(self):
        
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        
        self.tinfo.delete("1.0", tk.END)

        #Obtiene info de la ventana 'self.raiz':

        info1 = self.raiz.winfo_class()
        info2 = self.raiz.winfo_geometry()
        info3 = str(self.raiz.winfo_width())
        info4 = str(self.raiz.winfo_height())
        info5 = str(self.raiz.winfo_rootx())
        info6 = str(self.raiz.winfo_rooty())
        info7 = str(self.raiz.winfo_id())
        info8 = self.raiz.winfo_name()
        info9 = self.raiz.winfo_manager()

        # Construye una cadena de texto con toda la
        # información obtenida:
        
        texto_info = "Clase de 'raiz': " + info1 + "\n"
        texto_info += "Resolución y posición: " + info2 + "\n"
        texto_info += "Anchura ventana: " + info3 + "\n"
        texto_info += "Altura ventana: " + info4 + "\n"
        texto_info += "Pos. Ventana X: " + info5 + "\n"
        texto_info += "Pos. Ventana Y: " + info6 + "\n"
        texto_info += "Id. de 'raiz': " + info7 + "\n"
        texto_info += "Nombre objeto: " + info8 + "\n" 
        texto_info += "Gestor ventanas: " + info9 + "\n"

        # Inserta la información en la caja de texto:
        
        self.tinfo.insert("1.0", texto_info)

    def vista_new_recibo(self, vista):
        return 0


class add_recibo():
    '''Clase que contiene campos para crear Recibo'''

    def inicializar(self):
        self.raiz = tk.Tk()
        #define widget Text en el que se puede introducir textos
        self.tinfo = tk.Text(self.raiz, width = 80, height = 10)
        #situa la ventada en la parte superior
        self.tinfo.pack(side = tk.TOP)
        #boton info
        self.binfo = ttk.Button(self.raiz, text = 'Info', command = self.verinfo)
        self.binfo.pack(side =  tk.LEFT)        
        self.raiz.configure(bg = 'beige')
        self.raiz.title(TITULO)        
        self.bsalir = ttk.Button(self.raiz, text = 'Salir', command = self.raiz.destroy)
        self.bsalir.pack(side = tk.RIGHT)
        # El foco de la aplicación se sitúa en el botón
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        self.binfo.focus_set()
        self.raiz.mainloop()
        ttk.Label(self, text="Ingrese datos del Recibo", ).grid(
            row=1, column=2)
        ttk.Label(self, text="Cedula*: ").grid(row=2, column=1)
        ttk.Label(self, text="Nombre*: ").grid(row=3, column=1)
        ttk.Label(self, text="Apellido*: ").grid(row=4, column=1)
        ttk.Label(self, text="Direccion: ").grid(row=5, column=1)
        ttk.Label(self, text="Contactos*: ").grid(row=7, column=1)
        ttk.Label(self, text="tel.: ").grid(row=6, column=2)
        ttk.Label(self, text="email: ").grid(row=8, column=2)
        ttk.Label(self, text="Sueldo: ").grid(row=10, column=1)
        ttk.Button(self, text="GUARDAR", command = self.raiz.destroy).grid(row=11, column=3)

        # self.get_cedula_entry()
        # self.get_nombre_entry()
        # self.get_apellido_entry()
        # self.get_direccion_entry()
        # self.get_tel_entry()
        # self.get_email_entry()
        # self.get_sueldo_entry()



def main():
    tk.mi_app = vista_principal()
    return 0


main()