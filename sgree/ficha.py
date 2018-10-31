#-----------------------------------FICHA-------------------------------------------------

from abc import ABCMeta, abstractmethod

class Ficha(metaclass=ABCMeta):
    '''Clase abstracta Ficha'''
    @abstractmethod
    def __init__(self):
        pass

class Recibo(Ficha):
    def __init__(self, fecha, presupuesto, validez, tecnico, dispositivo):
        self.fecha = fecha
        self.presupuesto = presupuesto
        self.validez = validez
        self.tecnico = tecnico
        self.dispositivo = dispositivo