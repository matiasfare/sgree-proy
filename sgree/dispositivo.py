#---------------------------DISPOSITIVOS-------------------------------------------------------------
from abc import ABCMeta, abstractmethod

class Dispositivo(metaclass=ABCMeta):
    '''Dispositivo es una clase abstracta'''
    @abstractmethod
    def __init__(self, marca):
        self.marca = marca

class Celular (Dispositivo):
    '''Dispositivos tipo Celular'''
    def __init__ (self, marca, modelo, imeil):
        self.marca = marca
        self.modelo = modelo
        self.imeil = imeil
        

class Pc (Dispositivo):
    '''Dispositivos tipo PC de escritorio'''
    def __init__ (self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

        

class Notebook (Dispositivo):
    '''Dispositivos tipo Notebook o Laptop'''
    def __init__ (self, marca, modelo, dimencion_pantalla):
        self.marca = marca
        self.modelo = modelo
        self.dimencion_pantalla = dimencion_pantalla