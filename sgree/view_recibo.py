from tkinter import *
from tkinter import messagebox
# import base_de_datos as bd
from persona import Cliente
from ficha import Recibo
from contacto import *
from model import Model
from view_utils import *
import random
import sys, os, time
tipo = 'Recibos'

fondo = 'lime green'
buttom_color = 'lime green'

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
        Label(self, text="Dispositivo(imeil): ").grid(row = 7, column = 2 )
        Label(self, text="Cliente: ").grid(row = 8, column = 2)
        Button(self, text="GUARDAR", command = self.add_recibo, bg = buttom_color).grid(row = 15, column = 3,  sticky = W)

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
            
            Label(self, text=" "+ self.date).grid(row = 1, column = 3)
            # self.fecha_entry = Entry(master = self, width = 20)
            # self.fecha_entry.grid(row = 1 , column = 3)
            self.fecha_entry = self.date
            # print (self.date)
        return self.fecha_entry


    def get_observacion_entry(self):
        '''Cuadro de texto cliente-dato Observacion'''
        if not self.observacion_entry:
            self.observacion_entry = Entry(master = self, width = 20)
            self.observacion_entry.grid(row = 2, column = 2)
        return self.observacion_entry


    def get_validez_entry(self):
        '''Cuadro de texto cliente-dato Validez'''
        if not self.validez_entry:
            self.validez_entry = Entry(master = self, width = 20)
            self.validez_entry.grid(row = 3, column = 2)
        return self.validez_entry


    def get_tecnico_entry(self):
        '''Cuadro de texto cliente-dato Tecnico'''
        if not self.tecnico_entry:
            self.tecnico_entry = Entry(master = self, width = 20)
            self.tecnico_entry.grid(row = 4, column = 2)
        return self.tecnico_entry
    

    def get_presupuesto_entry(self):
        '''Cuadro de texto cliente-dato Presupuesto'''
        if not self.presupuesto_entry:
            self.presupuesto_entry = Entry(master = self, width = 20)
            self.presupuesto_entry.grid(row = 5, column = 2)
        return self.presupuesto_entry



    def get_dispositivo_entry(self):
        '''Cuadro de texto cliente-dato Dispositivo'''
        if not self.dispositivo_entry:
            self.dispositivo_entry = Entry(master = self, width = 20)
            self.dispositivo_entry.grid(row = 7, column = 3)
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
        if obs != "" and tec != "" and cli != "":
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
            fecha = self.date
            observacion = self.get_observacion_entry().get()
            validez = self.get_validez_entry().get()
            tecnico = self.get_tecnico_entry().get()
            presupuesto = self.get_presupuesto_entry().get()
            dispositivo = self.get_dispositivo_entry().get()
            cliente = self.get_cliente_entry().get()
            key = cliente

             
            
            if(self.val_recibo(fecha, observacion, validez, tecnico, cliente)):
                lista_rec = []
                recibo = Recibo(fecha, presupuesto, validez, tecnico, observacion, dispositivo)
                recibos = self.model.obtener_objetos(tipo)
                lista_rec.append(recibo)
                recibos[key] = lista_rec
                resul = self.model.guardar(recibos,key,tipo)
                if  resul == True :
                    messagebox.showinfo("", "Se Guardo con Exito")
                    self.destroy()
                elif resul == False:
                    messagebox.showinfo("", "Error, ya existe Recibo")
           
        except Exception as e:
            print(e)
            messagebox.showerror('Error', e)
        return True

class ViewDelRecibo(PanedWindow):
    '''Panel para borrar Cliente'''
    soli_entry = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.model = Model()
        self.pack()

    def inicializar(self):
        Label(self, text = "BORRAR RECIBO", ).grid(row = 1, column = 2)
        Label(self, text = "Ingrese numero RECIBO*: ").grid(row = 2, column = 1)
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
            key = int(self.get_soli_entry().get())
            try:
                if(messagebox.askyesno("Eliminar", "Eliminar cliente?")):
                    resul = self.model.eliminar_obj(str(key),tipo)
                    if(resul):
                        messagebox.showinfo("Eliminado", "Cliente eliminado")
                        self.destroy()
                    else:
                        messagebox.showerror("Info", "No existe cliente")
            except Exception as e:
                messagebox.showerror("Info", e)
        except:
            messagebox.showerror("Info", "Ingrese un numero Valido")


def list_recibos():
    """Genera una lista con los datos de los Recibos"""
    datos = ['------====== RECIBOS ======------']
    bucle = 1
    model = Model()
    recibos = {}
    recibos = model.obtener_objetos(tipo)
    print(recibos.keys())
    for key in recibos:
        # print(key.nombre)
        rec = recibos[key]
        datos.append("{}- Fecha: {}".format(bucle, rec.fecha))
        datos.append("     Cliente: {}".format(rec.cliente))
        datos.append("     Tecnico: {}".format(rec.tecnico))
        datos.append("     Presupuesto: {}".format(rec.presupuesto))        
        # datos.append("     Direccion: {}".format(rec.direccion))
        datos.append("     Observacion: ")
        # if rec.contactos:
        datos.append("     ----- : {}".format(rec.observacion))
            # datos.append("     -----Email: {}".format(rec.contactos.email))
        datos.append("")
        datos.append("")
        bucle += 1      
    list_datos(datos)



# root = Tk()

# ad = ViewNewRecibo(root)

# list_recibos()