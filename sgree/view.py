#Todo lo que sea Vista
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from view_cliente import *
from view_recibo import *
from controller import Controller

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

#Fuente y tamaño de Titulos
titulo = 'Helvetica 12 bold'
#Fuente y tamaño de texto
fuente = 'Helvetica 10 bold'

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
        menu_asesor.add_command(label="Cambiar Estado Recibo",
            command = self.edit_recibo )
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

#---------------Utils---------------------
    

    def salir(self):
        if(messagebox.askyesno("Salir", "Desea terminar la ejecucion?")):
            exit()

    def clear(self):
        if self.__vista_actual:
            self.__vista_actual.destroy()
    
    def info(self):
        messagebox.showinfo("Informacion","\n Info Temporal \n")

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
    
    def edit_recibo(self):
        self.clear()  
        form = ViewEditRecibo(self.__panel_master)
        self.__vista_actual = form

    # def listar_cliente(self):
    #     self.clear()  
    #     form = ViewDelCliente(self.__panel_master)
    #     self.__vista_actual = form

#------------------------Vistas Optener Datos---------------------

# class LabelLocal(Label):
#     '''Clase que genera objetos tipo Label'''
#     def __init__(self):
#         self.label = 
    
