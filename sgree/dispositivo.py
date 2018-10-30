#---------------------------DISPOSITIVOS-------------------------------------------------------------
from abc import ABCMeta, abstractmethod

class Dispositivo(metaclass=ABCMeta):
    '''Dispositivo es una clase abstracta'''
    @abstractmethod
    def __init__(self, marca):
        pass

class Celular (Dispositivo):
    '''Dispositivos tipo Celular'''
    def __init__ (self, marca, modelo, imeil):
        pass

class Pc (Dispositivo):
    '''Dispositivos tipo PC de escritorio'''
    def __init__ (sefl, marca, modelo, placa):
        pass

class Notebook (Dispositivo):
    '''Dispositivos tipo Notebook o Laptop'''
    def __init__ (sefl, marca, modelo, dimencion_pantalla):
        pass