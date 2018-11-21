from tkinter import *
from tkinter import messagebox
from persona import Cliente
from contacto import *
from model import Model
from view_utils import *
fondo = 'light blue'
buttombg = 'lime green'
tipo = 'Clientes'

class ViewNewCliente(PanedWindow):
    """Panel para introducir los datos de un cliente"""
    
    documento_entry = None
    nombre_entry = None
    apellido_entry = None
    direccion_entry = None
    tel_entry = None
    email_entry = None
    cliente = None
    
    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.start()
        self.pack()
        self.model = Model()

    def start(self):
        '''Inicializa ventana, agregar cliente'''
        self.__panel_master.config( bg =fondo)
        Label(self, text="Ingrese datos del Cliente").grid(row = 1, column = 2)
        Label(self, text="Cedula*: ").grid(row = 2, column = 1)
        Label(self, text="Nombre*: ").grid(row = 3, column = 1)
        Label(self, text="Apellido*: ").grid(row = 4, column = 1)
        Label(self, text="Telefono.*: ").grid(row = 5, column = 1)

        Label(self, text="DATOS OPCIONALES").grid(row=6, column=2)
        Label(self, text="Direccion: ").grid(row = 7, column =2 )
        Label(self, text="Email: ").grid(row = 8, column = 2)
        Button(self, text="GUARDAR", command = self.add_cliente, bg = buttombg).grid(row = 15, column = 3,  sticky = W)

        self.get_documento_entry()
        self.get_nombre_entry()
        self.get_apellido_entry()
        self.get_direccion_entry()
        self.get_tel_entry()
        self.get_email_entry()
    

    def get_documento_entry(self):
        '''Cuadro de texto cliente-dato documento'''
        if not self.documento_entry:
            self.documento_entry = Entry(master = self, width = 20)
            self.documento_entry.grid(row = 2 , column = 2)
        return self.documento_entry


    def get_nombre_entry(self):
        '''Cuadro de texto cliente-dato Nombre'''
        if not self.nombre_entry:
            self.nombre_entry = Entry(master = self, width = 20)
            self.nombre_entry.grid(row = 3, column = 2)
        return self.nombre_entry


    def get_apellido_entry(self):
        '''Cuadro de texto cliente-dato Apellido'''
        if not self.apellido_entry:
            self.apellido_entry = Entry(master = self, width = 20)
            self.apellido_entry.grid(row = 4, column = 2)
        return self.apellido_entry


    def get_tel_entry(self):
        '''Cuadro de texto cliente-dato Telefono'''
        if not self.tel_entry:
            self.tel_entry = Entry(master = self, width = 20)
            self.tel_entry.grid(row = 5, column = 2)
        return self.tel_entry
    

    def get_direccion_entry(self):
        '''Cuadro de texto cliente-dato Direccion'''
        if not self.direccion_entry:
            self.direccion_entry = Entry(master = self, width = 20)
            self.direccion_entry.grid(row = 7, column = 3)
        return self.direccion_entry



    def get_email_entry(self):
        '''Cuadro de texto cliente-dato Email'''
        if not self.email_entry:
            self.email_entry = Entry(master = self, width = 20)
            self.email_entry.grid(row = 8, column = 3)
        return self.email_entry


    def val_cli(self, doc, nom, ape):
        '''Valida los Datos del Nuevo Cliente'''
        val = False
        if doc.isdigit() and nom != "" and ape != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese correctamente los datos del " + "cliente")
        return val


    def val_cont(self, tel, mail):
        '''Valida datos Opcionales al agregar cliente'''
        val = False
        if tel != "" or mail != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese por lo menos 1 contacto")
        return val

    def add_cliente(self):
        '''Persiste el cliente nuevo'''
        try:
            documento = self.get_documento_entry().get()
            key = documento
            contacto = self.get_tel_entry().get()
            mail = self.get_email_entry().get()
            nombre = self.get_nombre_entry().get()
            apellido = self.get_apellido_entry().get()
            direccion = self.get_direccion_entry().get()
            if(self.val_cli(documento, nombre, apellido) and self.val_cont(contacto, mail)):
                cliente = Cliente(documento,nombre, apellido, contacto)
                resul = self.model.guardar(cliente,key,tipo)
                if  resul == True :
                    messagebox.showinfo("", "Se Guardo con Exito")
                    self.destroy()
                elif resul == False:
                    messagebox.showinfo("", "Error, ya existe Cliente")
           
        except Exception as e:
            messagebox.showerror('Error', e)
        return True

class ViewDelCliente(PanedWindow):
    '''Panel para borrar Cliente'''
    soli_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.model = Model()
        self.pack()

    def inicializar(self):
        Label(self, text = "BORRAR CLIENTE", ).grid(row = 1, column = 2)
        Label(self, text = "Ingrese numero de CI del cliente*: ").grid(row = 2, column = 1)
        Button(self, text = "Eliminar", command = self.eliminar).grid(
            row = 3, column = 1)

        self.get_soli_entry()

    def get_soli_entry(self):
        if not self.soli_entry:
            self.soli_entry = Entry(master = self, width = 20)
            self.soli_entry.grid(row = 2, column = 2)
        return self.soli_entry

    def eliminar(self):
        try:
            key = self.get_soli_entry().get()
            if(messagebox.askyesno("Eliminar", "Eliminar cliente?")):
                self.model.eliminar_obj(key,tipo)
                messagebox.showinfo("Eliminado", "Cliente eliminado")
                self.destroy()
        except:
            messagebox.showerror("Info", "No existe cliente")
        


def list_cliente():
    """Genera una lista con los datos de los clientes"""
    datos = ['------======DETALLE CLIENTES======------']
    bucle = 1
    model = Model()
    clientes = model.obtener_objetos(tipo)
    print(clientes)
    for key in clientes:
        cli = clientes[key]
        datos.append("{}- Cedula: {}".format(bucle, cli.documento))
        datos.append("     Nombre: {}".format(cli.nombre))
        datos.append("     Apellido: {}".format(cli.apellido))
        # datos.append("     Direccion: {}".format(cli.direccion))
        datos.append("     Contactos: ")
        # if cli.contactos:
        datos.append("     -----Tel: {}".format(cli.contacto))
            # datos.append("     -----Email: {}".format(cli.contactos.email))
        datos.append("")
        datos.append("")
        bucle += 1        
    list_datos(datos)