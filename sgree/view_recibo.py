from tkinter import *
from tkinter import messagebox
# import base_de_datos as bd
from persona import Cliente
from ficha import Recibo
from contacto import *
from model import Model
import view as utils
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
        Label(self, text="NUEVO RECIBO: ", font = utils.titulo).grid(row = 1, column = 1)
        Label(self, text="Fecha-Recibo: " , font = utils.fuente).grid(row = 1, column = 2)
        Label(self, text="Observacion*: ", font = utils.fuente).grid(row = 2, column = 1)
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
            self.fecha_entry = self.date
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


    def val_cont(self, tel, mail):
        '''Valida datos Opcionales al agregar cliente'''
        val = False
        if tel != "" or mail != "":
            val = True
        else:
            messagebox.showinfo("", "Ingrese Todos los Datos requeridos")
        return val
   
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
            estado = 'Pendiente'
             
            
            if(self.val_recibo(fecha, observacion, validez, tecnico, cliente) and self.val_cont(dispositivo,cliente)):
                recibo = Recibo(fecha, presupuesto, validez, tecnico, observacion, dispositivo,cliente,estado)
                resul = self.model.guardar(recibo,recibo.get_clave())
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
        tipo = 'Recibos'
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

class ViewEditRecibo(PanedWindow):
    '''Panel para Editar Cliente'''
    soli_entry = None
    opcion = None

    def __init__(self, panel_master):
        PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.model = Model()
        self.pack()
        


    def inicializar(self):
        
        Label(self, text = "ACTUALIZAR RECIBO", ).grid(row = 1, column = 2)
        Label(self, text = "Ingrese Codigo RECIBO*: ").grid(row = 2, column = 1)
        Label(self, text = "Ingrese nuevo estado*: ").grid(row = 3, column = 1)
        Label(self, text = "Estados Validos: Retirado, Pendiente, Presupuesto ").grid(row = 4, column = 1)

        Button(self, text = "Cargar Cambio", command = self.editar).grid(
            row = 4, column = 2)
        


        self.get_cod_entry()
        self.get_estado_entry()

    def get_cod_entry(self):
        if not self.soli_entry:
            self.soli_entry = Entry(master = self, width = 10)
            self.soli_entry.grid(row = 2, column = 2)
        return self.soli_entry


    def get_estado_entry(self):
        if not self.opcion:
            self.opcion = Entry(master = self, width = 15)
            self.opcion.grid(row = 3, column = 2)
        return self.opcion      


    def editar(self):
        try:
            key = int(self.get_cod_entry().get())
            new_status = self.get_estado_entry().get()
            #Comprueba que el codigo exista
            recibos = self.model.obtener_objetos(Recibo)
            can_reci= len(recibos)
            try:
                if key >= 0 and key <= can_reci:
                    if(messagebox.askyesno("Editar", "Editar Recibo?")):
                        reci = recibos[key]
                        reci.estado = new_status
                        resul = self.model.update(reci,key)
                    elif (resul):
                        messagebox.showinfo("Editar", "Edicion Finalizada")
                    else:
                        messagebox.showinfo("Editar", "Edicion Cancelada")
                else:
                    messagebox.showerror("Info", "No existe Recibo")
            except Exception as e:
                messagebox.showerror("Info", e)
        except:
            messagebox.showerror("Info", "Ingrese un numero Valido \n o Existente")


# def list_recibos():
#     """Genera una lista con los datos de los Recibos"""
#     datos = ['################ RECIBOS ###############']
#     bucle = 1
#     model = Model()
#     recibos = []
#     recibos = model.obtener_objetos(Recibo)
    
#     for rec in recibos:
#         datos.append("{}- Fecha: {}".format(bucle, rec.fecha))
#         datos.append("     Codigo : {}".format(recibos.index(rec)))
#         datos.append("     Cliente: {}".format(rec.cliente))
#         datos.append("     Tecnico: {}".format(rec.tecnico))
#         datos.append("     Presupuesto: {}".format(rec.presupuesto))
#         datos.append("     Validez: {} Dias".format(rec.validez))
#         datos.append("     Vencido: {}".format(rec.calcular_validez()))
#         datos.append("     Observacion: ")
#         datos.append("     ----- : {}".format(rec.observacion))
#         datos.append("     Estado: {}".format(rec.estado))
#         datos.append("")
#         datos.append("")
#         bucle += 1      
#     list_datos(datos)



# root = Tk()

# # ad = ViewNewRecibo(root)

# list_recibos()