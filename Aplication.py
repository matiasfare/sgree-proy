from Ficha import Recibo 
from ZODB import FileStorage, DB
from Persona import Cliente
from Dispositivo import Celular, Pc, Notebook
from Control import input_num
import persistent, os

storage = FileStorage.FileStorage("datasys/sgree-data.fs")
db = DB(storage)
connection = db.open()
root = connection.root

class Aplication (persistent.Persistent,Cliente ,Celular):
    
    def imprimir_recibo(self):
        pass

def mostrar_menu():
    os.system('clear')
    print('Indique lo que desera realizar:')
    print('--------------------------------')
    print('Crear Recibo (1)')
    print('Buscar       (2)')
    print('Listar       (3)')
    print('Editar Ficha (4)')

def input_menu(opcion):
    opciones = [crear_recibo(), buscar(), listar(), editar_ficha()]
    print(opciones[opcion])
    
    

while True:
    #Muestra opciones del menu
    mostrar_menu()
    opcion = input("ingrese opcion:")
    input_menu(opcion)

db.close()