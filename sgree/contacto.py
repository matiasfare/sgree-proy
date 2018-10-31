#-----------------------------------CONTACTO-------------------------------------------------
from abc import ABCMeta, abstractmethod

class Contacto(metaclass=ABCMeta):
    '''Contacto es una clase abstracta'''
    @abstractmethod
    def __init__(self, nombre):
        pass


class Sucursal(Contacto):
    '''Clase sucursal'''
    pass


class Email(Contacto):
    '''Clase Email'''
    pass


class Direccion(Contacto):
    '''Clase Drección'''
    pass