# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from persona import *
from model import *

bgC = "black"
fgC = "black"
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


# def list_asesor():
#     """Genera una lista con los datos de los asesores"""
#     datos = ['------======DETALLE ASESORES======------']
#     bucle = 1
#     for asesor in bd.asesores:
#         datos.append("{}- Cedula: {}".format(bucle, asesor.cedula))
#         datos.append("     Nombre: {}".format(asesor.nombre))
#         datos.append("     Apellido: {}".format(asesor.apellido))
#         datos.append("     Direccion: {}".format(asesor.direccion))
#         datos.append("     Contactos: ")
#         if asesor.contactos:
#             datos.append("     -----Tel: {}".format(asesor.contactos.tel))
#             datos.append("     -----Email: {}".format(asesor.contactos.email))
#         datos.append("     Fecha Inicio: {}".format(asesor.fecha_ini))
#         datos.append("     Sueldo: {}".format(asesor.sueldo))
#         datos.append("")
#         datos.append("")
#         bucle += 1
#     list_datos(datos)
    
# def list_soli(soli):
#     """Genera una lista con los datos de las solicitudes"""
#     datos = ['------======DETALLE SOLICITUDES======------']
#     bucle = 1
#     ep = "                  "
#     ep1 = "                                      "
#     for sol in soli:
#         datos.append("{}- Cliente: {}".format(bucle, sol.cliente))
#         datos.append("     Asesor: {}".format(sol.asesor))
#         datos.append("     Vehiculo: ")
#         datos.append("{}-Chapa: {}".format(ep, sol.vehiculo.chapa))
#         datos.append("{}-Marca: {}".format(ep, sol.vehiculo.marca))
#         datos.append("{}-Modelo: {}".format(ep, sol.vehiculo.modelo))
#         datos.append("     Repuestos:".format(ep))
#         if sol.repuestos:
#             datos.append("{}=Tipo: {}".format(ep, sol.repuestos.tipo))
#             datos.append("{}=Marca: {}".format(ep, sol.repuestos.marca))
#             datos.append("{}=Costo: {}".format(ep, sol.repuestos.costo))
#             datos.append("")
#         datos.append("")
#         bucle += 1
#     list_datos(datos)
    
# def list_bajas():
#     """Genera una lista con los datos de las solicitudes procesadas"""
#     list_soli(bd.solicitudes_baja)

# def list_nobajas():
#     """Genera una lista con los datos de las solicitudes no procesadas"""
#     list_soli(bd.solicitudes)