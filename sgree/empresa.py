#-----------------------------------EMPRESA-------------------------------------------------
from abc import ABCMeta, abstractmethod
# from Ficha import * 
# from ZODB import FileStorage, DB
# from Persona import Cliente
# from Dispositivo import Celular, Pc, Notebook

class Empresa(metaclass=ABCMeta):
    '''Ficha es una clase abstracta'''
    @abstractmethod
    def __init__(self, nombre):
        pass


class Sucursal(Empresa):
    '''clase que contiene menus y funciones que modifican los datos de la Sucursal'''
    def __init__ (self, nombre, tecnicos):
        self.nombre = nombre
        self.tecnicos = tecnicos
        self.recibos = recibos
        pass