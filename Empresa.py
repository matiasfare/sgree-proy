from abc import ABCMeta, abstractmethod
from Ficha import * 
from ZODB import FileStorage, DB
from Persona import Cliente
from Dispositivo import Celular, Pc, Notebook


# storage = FileStorage.FileStorage("datasys/sgree-data.fs")
# db = DB(storage)
# connection = db.open()
# root = connection.root


class Empresa(metaclass=ABCMeta):
    '''Ficha es una clase abstracta'''
    @abstractmethod
    def __init__(self, nombre):
        pass


class Sucursal(Empresa):
	'''clase que contiene menus y funciones que modifican los datos de la Sucursal'''
    def __init__ (self, nombre, tecnicos[], recibos[]):
    	self.nombre = nombre
    	self.tecnicos = tecnicos
    	self.recibos = recibos


afcompany.()	


# class Aplication (persistent.Persistent,Cliente ,Celular):
    
#     def imprimir_recibo(self):s
#         pass

# def mostrar_menu():
#     os.system('clear')
#     print('Indique lo que desera realizar:')
#     print('--------------------------------')
#     print('Crear Recibo (1)')
#     print('Buscar       (2)')
#     print('Listar       (3)')
#     print('Editar Ficha (4)')


# def input_num():
#     numerico = False
#     num = 0
#     while(not numerico):
#         try:
#             num = input(int())
#             numerico = True
#         except ValueError:
#             print("Error, Ingrese una opcion valida: ")
#     return num
    


# opcion = input("ingrese opcion:")
# #sale de la aplicacion
# def quit():
#   raise SystemExit()

# #diccionario de opciones
# opciones = {

#     }

# mostrar_menu()

# db.close()