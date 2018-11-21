from tkinter import *
from tkinter import messagebox
# import base_de_datos as bd
from persona import Cliente
from ficha import Recibo
from contacto import *
from model import Model
import sys, os, time
tipo = 'Recibos'

fondo = 'light blue'
button_color = 'lime green'

class ViewNewRecibo(PanedWindow):
    '''Panel para crear un Recibo'''

    date = time.strftime("%F")
    model = Model()
    fecha_entry = None
    observacion_entry = None
    validez_entry = None
    tecnico_entry = None
    presupuesto_entry = None
    dispositivo_entry = None
    cliente_entry = None
    
    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.start()
        self.pack()
        self.model = Model()


    def start(self):
        '''Inicializa ventana, agregar cliente'''
        self.__panel_master.config( bg =fondo)
        Label(self, text="NUEVO RECIBO: ").grid(row = 1, column = 1)
        Label(self, text="Fecha-Recibo: ").grid(row = 1, column = 2)
        Label(self, text="Observacion*: ").grid(row = 2, column = 1)
        Label(self, text="Validez*: ").grid(row = 3, column = 1)
        Label(self, text="Tecnico*: ").grid(row = 4, column = 1)
        Label(self, text="Presupuesto*: ").grid(row = 5, column = 1)

        Label(self, text="----------IMPORTANTE----------").grid(row = 6, column = 2)
        Label(self, text="Dispositivo: ").grid(row = 7, column = 2 )
        Label(self, text="Cliente: ").grid(row = 8, column = 2)
        Button(self, text="GUARDAR", command = self.add_recibo, bg = button_color).grid(row = 15, column = 3,  sticky = W)

        self.get_fecha_entry()
        self.get_observacion_entry()
        self.get_validez_entry()
        self.get_tecnico_entry()
        self.get_presupuesto_entry()
        self.get_dispositivo_entry()
        self.get_cliente_entry()
    

    def get_fecha_entry(self):
        '''Cuadro de texto cliente-dato fecha'''
        if not self.fecha_entry:
            self.fecha_entry = Entry(master = self, width = 20)
            self.fecha_entry.grid(row = 1 , column = 3)
            self.fecha_entry = self.date
            print (self.date)
        return self.fecha_entry


    def get_observacion_entry(self):
        '''Cuadro de texto cliente-dato Observacion'''
        if not self.observacion_entry:
            self.observacion_entry = Entry(master = self, width = 20)
            self.observacion_entry.grid(row = 3, column = 2)
        return self.observacion_entry


    def get_validez_entry(self):
        '''Cuadro de texto cliente-dato Validez'''
        if not self.validez_entry:
            self.validez_entry = Entry(master = self, width = 20)
            self.validez_entry.grid(row = 4, column = 2)
        return self.validez_entry


    def get_tecnico_entry(self):
        '''Cuadro de texto cliente-dato Tecnico'''
        if not self.tecnico_entry:
            self.tecnico_entry = Entry(master = self, width = 20)
            self.tecnico_entry.grid(row = 5, column = 2)
        return self.tecnico_entry
    

    def get_presupuesto_entry(self):
        '''Cuadro de texto cliente-dato Presupuesto'''
        if not self.presupuesto_entry:
            self.presupuesto_entry = Entry(master = self, width = 20)
            self.presupuesto_entry.grid(row = 7, column = 3)
        return self.presupuesto_entry



    def get_dispositivo_entry(self):
        '''Cuadro de texto cliente-dato Dispositivo'''
        if not self.dispositivo_entry:
            self.dispositivo_entry = Entry(master = self, width = 20)
            self.dispositivo_entry.grid(row = 8, column = 3)
        return self.dispositivo_entry
    
    def get_cliente_entry(self):
        '''Cuadro de texto cliente-dato Cliente'''
        if not self.cliente_entry:
            self.cliente_entry = Entry(master = self, width = 20)
            self.cliente_entry.grid(row = 8, column = 3)
        return self.cliente_entry


    def val_recibo(self, fecha, obs, vali, tec, cli):
        '''Valida los Datos del Nuevo Recibo'''
        val = False
        if vali.isdigit() and obs != "" and tec != "" and cli != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese correctamente los datos del " + "Recibo")
        return val


    # def val_cont(self, tel, mail):
    #     '''Valida datos Opcionales al agregar cliente'''
    #     val = False
    #     if tel != "" or mail != "":
    #         val = True
    #     else:
    #         messagebox.showinfo("", "Ingrese por lo menos 1 contacto")
    #     return val

    def add_recibo(self):
        '''Persiste nuevo Recibo, si esta correctamente cargado'''
        try:
            fecha = self.get_fecha_entry().get()
            observacion = self.get_observacion_entry().get()
            validez = self.get_validez_entry().get()
            tecnico = self.get_tecnico_entry().get()
            presupuesto = self.get_presupuesto_entry().get()
            dispositivo = self.get_dispositivo_entry().get()
            cliente = self.get_cliente_entry().get()
            key = cliente
             
            
            if(self.val_recibo(fecha, observacion, validez, tecnico, cliente)):
                recibo = Recibo(fecha, presupuesto, validez, tecnico, observacion, dispositivo)
                resul = self.model.guardar(recibo,key,tipo)
                if  resul == True :
                    messagebox.showinfo("", "Se Guardo con Exito")
                    self.destroy()
                elif resul == False:
                    messagebox.showinfo("", "Error, ya existe Recibo")
           
        except Exception as e:
            messagebox.showerror('Error', e)
        return True