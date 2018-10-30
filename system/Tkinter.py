#Tkinter.py
#Se ubasa la lib. Tkinter para la persistencia de Datos
import tkinter
from Tkinter import *
from Tkinter import Message
from Controller import Controller

top = Tkinter.Tk()
top.title("Interfaz de personas")

def listarPersonas():
    c = Controller()
    listado = 'Lista de personas en la base de datos: \n'
    root = Tk()
    text = Text(root)
    root.title("Listado de Personas")
    text.insert(INSERT, listado)
    items = c.listarPersonas()
    for i in items:
        text.insert(INSERT, 'Nombre: '+i.nombre+', Apellido: '+i.apellido+', Documento: '+ str(i.documento)+'\n')
    text.pack()
	
def buscarPersonas():
    rootBuscar = Tk()
    text = Text(rootBuscar)
    rootBuscar.title("buscar Personas")
	
	
Boton1 = Tkinter.Button(top, text = "Listar Personas", command = listarPersonas)
Boton2 = Tkinter.Button(top, text = "Buscar Persona", command = buscarPersonas)

Boton1.pack()
Boton2.pack()
top.mainloop()
