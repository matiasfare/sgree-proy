#-----------------------------------EMPRESA-------------------------------------------------
from abc import ABCMeta, abstractmethod
class Empresa(metaclass=ABCMeta):
    '''Ficha es una clase abstracta'''
    @abstractmethod
    def __init__(self, nombre):
        pass


class Sucursal(Empresa):
    '''Clase sucursal'''
    recibos = []       
    def __init__ (self, nombre, tecnicos, recibos):
        self.nombre = nombre
        self.tecnicos = tecnicos
        self.recibos.append(recibos)