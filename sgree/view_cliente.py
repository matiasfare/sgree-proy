from tkinter import *
from tkinter import messagebox
# import base_de_datos as bd
from persona import Cliente
from contacto import *
import controller as ct
bgC = 'light blue'
buttom = 'light greep'

class VistaNewCliente(PanedWindow):
    """Panel que contien los campos para introducir los datos de un cliente"""

    cedula_entry = None
    nombre_entry = None
    apellido_entry = None
    direccion_entry = None
    tel_entry = None
    email_entry = None
    ruc_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.start()
        self.pack()

    def start(self):
        self.__panel_master.config(bg=bgC)
        Label(self, text="Ingrese datos del Cliente").grid(row=1, column=2)
        Label(self, text="Cedula*: ").grid(row = 2, column = 1)
        Label(self, text="Nombre*: ").grid(row = 3, column = 1)
        Label(self, text="Apellido*: ").grid(row = 4, column = 1)
        Label(self, text="Telefono.*: ").grid(row = 5, column = 1)

        Label(self, text="DATOS OPCIONALES").grid(row=6, column=2)
        Label(self, text="Direccion: ").grid(row = 7, column =2 )
        Label(self, text="Email: ").grid(row = 8, column = 2)
        Button(self, text="GUARDAR", command = self.crear_objeto).grid(row = 15, column = 3)

        

        self.get_cedula_entry()
        self.get_nombre_entry()
        self.get_apellido_entry()
        self.get_direccion_entry()
        self.get_tel_entry()
        self.get_email_entry()
    

    def get_cedula_entry(self):
        if not self.cedula_entry:
            self.cedula_entry = Entry(master = self, width = 20)
            self.cedula_entry.grid(row = 2 , column = 2)
        return self.cedula_entry


    def get_nombre_entry(self):
        if not self.nombre_entry:
            self.nombre_entry = Entry(master = self, width = 20)
            self.nombre_entry.grid(row = 3, column = 2)
        return self.nombre_entry


    def get_apellido_entry(self):
        if not self.apellido_entry:
            self.apellido_entry = Entry(master = self, width = 20)
            self.apellido_entry.grid(row = 4, column = 2)
        return self.apellido_entry


    def get_tel_entry(self):
        if not self.tel_entry:
            self.tel_entry = Entry(master = self, width = 20)
            self.tel_entry.grid(row = 5, column = 2)
        return self.tel_entry
    

    def get_direccion_entry(self):
        if not self.direccion_entry:
            self.direccion_entry = Entry(master = self, width = 20)
            self.direccion_entry.grid(row = 7, column = 3)
        return self.direccion_entry



    def get_email_entry(self):
        if not self.email_entry:
            self.email_entry = Entry(master = self, width = 20)
            self.email_entry.grid(row = 8, column = 3)
        return self.email_entry


    def val_cli(self, ced, nom, ape):
        val = False
        if ced.isdigit() and nom != "" and ape != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese correctamente los datos del " +
                "cliente")
        return val


    def val_cont(self, tel, mail):
        val = False
        if tel != "" or mail != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese por lo menos 1 contacto")
        return val

    def crear_objeto(self):
        try:
            contacto = self.get_tel_entry().get()
            mail = self.get_email_entry().get()
            documento = self.get_cedula_entry().get()
            nombre = self.get_nombre_entry().get()
            apellido = self.get_apellido_entry().get()
            direccion = self.get_direccion_entry().get()
            if(self.val_cli(documento, nombre, apellido) and self.val_cont(contacto, mail)):
                new_cliente = Cliente(documento,nombre, apellido, contacto)
        except Exception as e:
            messagebox.showerror('Error', e)
        return new_cliente