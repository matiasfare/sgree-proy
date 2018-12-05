# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from controller import Controller
from persona import *
from model import *

bgBC = "white"
resol_pc_vs = '600x300+200+160'


def list_datos(datos):
    """Genera una ventana que muestra los datos de una lista con scrollbar"""
    ventana = Tk()
    ventana.title("Lista")
    ventana.resizable(0, 0)
    ventana.geometry(resol_pc_vs)

    Label(ventana, text="DETALLES", ).pack()

    def colocar_scrollbar(listbox, scrollbar):
        scrollbar.config(command=listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.pack(side=LEFT, fill=Y)

    frame1 = Frame(ventana, bd=5, height=600, width=350)
    frame1.pack()
    scroll1 = Scrollbar(frame1)
    list1 = Listbox(frame1, width=70, height=20)
    list1.pack()
    colocar_scrollbar(list1, scroll1)

    def cargarlistbox(lista, listbox):
        ind, largo = 0, len(lista)
        while ind < largo:
            listbox.insert(END, lista[ind])
            ind += 1

    #ventana.focus_set()
    #ventana.grab_set()
    #ventana.overrideredirect(1)

    cargarlistbox(datos, list1)
    ventana.mainloop()


def list_recibos():
    """Genera una lista con los datos de todos los Recibos"""
    datos = ['################ RECIBOS ###############']
    bucle = 1
    model = Model()
    recibos = []
    recibos = model.obtener_objetos(Recibo)
    
    for rec in recibos:
        datos.append("{}- Fecha: {}".format(bucle, rec.fecha))
        datos.append("     Codigo : {}".format(recibos.index(rec)))
        datos.append("     Cliente: {}".format(rec.cliente))
        datos.append("     Tecnico: {}".format(rec.tecnico))
        datos.append("     Presupuesto: {}".format(rec.presupuesto))
        datos.append("     Validez: {} Dias".format(rec.validez))
        datos.append("     Valido: {}".format(rec.calcular_validez()))
        datos.append("     Observacion: ")
        datos.append("     ----- : {}".format(rec.observacion))
        datos.append("     Estado: {}".format(rec.estado))
        datos.append("")
        datos.append("")
        bucle += 1      
    list_datos(datos)

def filtrar_recibos_tecnico(dato):
    '''Devuelve lista de objetos que cumpla con los requisitos del recibo'''
    model = Model()
    recibos = model.obtener_objetos(Recibo)
    lista = []
    print('Hola')
    try:
        for rec in recibos:
            if rec.tecnico == dato:
                lista.append(copy.copy(rec))
    except Exception as e:
        print(e)
        
    return lista
            



def list_por_dato_recibido(dato):
    """Genera una lista con los datos de todos los Recibos Por el Tecnico que Recibe"""
    datos = ['################ RECIBOS ###############']
    bucle = 1
    model = Model()
    recibos = []
    recibos = model.obtener_objetos(Recibo)
    
    for rec in recibos:
        if rec.tecnico == dato:
            datos.append("{}- Fecha: {}".format(bucle, rec.fecha))
            datos.append("     Codigo : {}".format(recibos.index(rec)))
            datos.append("     Cliente: {}".format(rec.cliente))
            datos.append("     Tecnico: {}".format(rec.tecnico))
            datos.append("     Presupuesto: {}".format(rec.presupuesto))
            datos.append("     Validez: {} Dias".format(rec.validez))
            datos.append("     Valido: {}".format(rec.calcular_validez()))
            datos.append("     Observacion: ")
            datos.append("     ----- : {}".format(rec.observacion))
            datos.append("     Estado: {}".format(rec.estado))
            datos.append("")
            datos.append("")
            bucle += 1      
    list_datos(datos)



def list_cliente():
    """Genera una lista con los datos de los clientes"""
    datos = ['########### CLIENTES ############']
    bucle = 1
    model = Model()
    clientes = []
    clientes = model.obtener_objetos(Cliente)
    for cli in clientes:
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


