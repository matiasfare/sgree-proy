#Todo lo que sea Vista
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from view_cliente import *
from view_recibo import *

from tkinter import ttk


#Resolucion y pocicion de Ventana Principal
    #Principal
resol_poc_vp = '500x250+200+150'
    #Secundaria
resol_pc_vs = '600x300+200+160'
TITULO = 'SGREE - Proyecto Paradigmas'
#Color de la Ventana
fondo = "Beige"
buttom_color = 'lime green'

class View(Frame):

    '''Clase que contiene pantalla principal, y las llamadas a las funciones u otras vistas'''

    __vista_actual = None

    def __init__ (self, panel_master):
        Frame.__init__(self, panel_master)
        self.__panel_master = panel_master
        self.start()
        self.pack()

    def start(self):
        
        self.__panel_master.geometry(resol_poc_vp)
        self.__panel_master.title(TITULO)
        self.__panel_master.protocol("WM_DELETE_WINDOW", "onexit")
        self.__panel_master.resizable(0, 0)
        self.__panel_master.config(bg=fondo)
        menubar = Menu(self.__panel_master)
        self.__panel_master.config(menu=menubar)

        menu_cliente = Menu(menubar, tearoff=0)
        menu_cliente.add_command(label="Agregar cliente",
            command = self.add_cliente)
        menu_cliente.add_command(label="Eliminar cliente",
            command = self.del_cliente)
        menu_cliente.add_command(label="Listar clientes", 
            command = list_cliente)
        menubar.add_cascade(label="Clientes", menu = menu_cliente)

        menu_asesor = Menu(menubar, tearoff=0)
        menu_asesor.add_command(label="Crear Recibo",
            command = self.add_recibo)
        menu_asesor.add_command(label="Eliminar Recibo",
            command = self.del_recibo)
        menu_asesor.add_command(label="Listar Recibos",
            command = list_recibos)
        menubar.add_cascade(label="Recibos", menu = menu_asesor)

        menu_soli = Menu(menubar, tearoff=0)
        menu_soli.add_command(label = "Por Técnico", 
            command = self.info)
        menu_soli.add_command(label = "Por Fecha", 
            command = self.info)
        menu_soli.add_separator()
        menu_soli.add_command(label = "Por Cliente",
            command = self.info)
        menubar.add_cascade(label = "Listar Registros", menu = menu_soli)
        
        menu_ayuda = Menu(menubar, tearoff = 0)
        menu_ayuda.add_separator()
        menu_ayuda.add_command(label = "Acerca del sistema", 
            command = self.info)
        menu_ayuda.add_separator()
        menubar.add_cascade(label = "Ayuda", 
            menu = menu_ayuda)

        menubar.add_command(label = "Salir", command = self.salir)

    
    # def ver_info(self):
        
    #     # Borra el contenido que tenga en un momento dado
    #     # la caja de texto
        
    #     self.tinfo.delete("1.0", tk.END)

    #     #Obtiene info de la ventana 'self.raiz':

    #     info1 = self.raiz.winfo_class()
    #     info2 = self.raiz.winfo_geometry()
    #     info3 = str(self.raiz.winfo_width())
    #     info4 = str(self.raiz.winfo_height())
    #     info5 = str(self.raiz.winfo_rootx())
    #     info6 = str(self.raiz.winfo_rooty())
    #     info7 = str(self.raiz.winfo_id())
    #     info8 = self.raiz.winfo_name()
    #     info9 = self.raiz.winfo_manager()

    #     # Construye una cadena de texto con toda la
    #     # información obtenida:
        
    #     texto_info = "Clase de 'raiz': " + info1 + "\n"
    #     texto_info += "Resolución y posición: " + info2 + "\n"
    #     texto_info += "Anchura ventana: " + info3 + "\n"
    #     texto_info += "Altura ventana: " + info4 + "\n"
    #     texto_info += "Pos. Ventana X: " + info5 + "\n"
    #     texto_info += "Pos. Ventana Y: " + info6 + "\n"
    #     texto_info += "Id. de 'raiz': " + info7 + "\n"
    #     texto_info += "Nombre objeto: " + info8 + "\n" 
    #     texto_info += "Gestor ventanas: " + info9 + "\n"

    #     # Inserta la información en la caja de texto:
        
    #     self.tinfo.insert("1.0", texto_info)

    # def vista_new_recibo(self, vista):
    #     return 0


# class add_recibo():
#     '''Clase que contiene campos para crear Recibo'''

#     def inicializar(self):
#         self.raiz = tk.Tk()
#         #define widget Text en el que se puede introducir textos
#         self.tinfo = tk.Text(self.raiz, width = 80, height = 10)
#         #situa la ventada en la parte superior
#         self.tinfo.pack(side = tk.TOP)
#         #boton info
#         self.binfo = ttk.Button(self.raiz, text = 'Info', command = self.verinfo)
#         self.binfo.pack(side =  tk.LEFT)        
#         self.raiz.configure(bg = 'beige')
#         self.raiz.title(TITULO)        
#         self.bsalir = ttk.Button(self.raiz, text = 'Salir', command = self.raiz.destroy)
#         self.bsalir.pack(side = tk.RIGHT)
#         # El foco de la aplicación se sitúa en el botón
#         # 'self.binfo' resaltando su borde. Si se presiona
#         # la barra espaciadora el botón que tiene el foco
#         # será pulsado. El foco puede cambiar de un widget
#         # a otro con la tecla tabulador [tab]
#         self.binfo.focus_set()
#         self.raiz.mainloop()
#         ttk.Label(self, text="Ingrese datos del Recibo", ).grid(
#             row=1, column=2)
#         ttk.Label(self, text="Cedula*: ").grid(row=2, column=1)
#         ttk.Label(self, text="Nombre*: ").grid(row=3, column=1)
#         ttk.Label(self, text="Apellido*: ").grid(row=4, column=1)
#         ttk.Label(self, text="Direccion: ").grid(row=5, column=1)
#         ttk.Label(self, text="Contactos*: ").grid(row=7, column=1)
#         ttk.Label(self, text="tel.: ").grid(row=6, column=2)
#         ttk.Label(self, text="email: ").grid(row=8, column=2)
#         ttk.Label(self, text="Sueldo: ").grid(row=10, column=1)
#         ttk.Button(self, text="GUARDAR", command = self.raiz.destroy).grid(row=11, column=3)

#         # self.get_cedula_entry()
#         # self.get_nombre_entry()
#         # self.get_apellido_entry()
#         # self.get_direccion_entry()
#         # self.get_tel_entry()
#         # self.get_email_entry()
#         # self.get_sueldo_entry()


#---------------Utils---------------------
    def salir(self):
        if(messagebox.askyesno("Salir", "Desea terminar la ejecucion?")):
            exit()

    def clear(self):
        if self.__vista_actual:
            self.__vista_actual.destroy()
    
    def info(self):
        messagebox.showinfo("Informacion","\n Info Temporal \n")

#-----------------------------------------------------------

#     def vista_agregar_cliente(self):
#         '''Intereactua con le usuario asi obtener datos necesarios para crear objeto Cliente '''
#         print("----------CREAR CLIENTE-------------!\n")
#         cedula  = input("Ingrese documento del nuevo Cliente: ")
#         nombre = input("Ingrese el nombre del nuevo Cliente:")
#         apellido = input("ingrese el apellido del nuevo Cliente:")
#         contacto = input ("Ingrese numero de contacto: ")
#         nuevo_cliente = Cliente(cedula, nombre, apellido, contacto)
#         return nuevo_cliente

# -----------------Call Frames /// Controller----------------------


    def add_cliente(self):
        self.clear()  
        form = ViewNewCliente(self.__panel_master)
        self.__vista_actual = form

    def add_recibo(self):
        self.clear()  
        form = ViewNewRecibo(self.__panel_master)
        self.__vista_actual = form
    
    def del_cliente(self):
        self.clear()  
        form = ViewDelCliente(self.__panel_master)
        self.__vista_actual = form

    def del_recibo(self):
        self.clear()  
        form = ViewDelRecibo(self.__panel_master)
        self.__vista_actual = form

    # def listar_cliente(self):
    #     self.clear()  
    #     form = ViewDelCliente(self.__panel_master)
    #     self.__vista_actual = form

#------------------------Vistas Optener Datos---------------------


