from abc import ABCMeta, abstractmethod
# from Ficha import * 
# from ZODB import FileStorage, DB
# from Persona import Cliente
# from Dispositivo import Celular, Pc, Notebook


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
    def __init__ (self, nombre, tecnicos, recibos):
        self.nombre = nombre
        self.tecnicos = tecnicos
        self.recibos = recibos
        pass
