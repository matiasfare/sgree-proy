#-----------------------------------FICHA-------------------------------------------------

from abc import ABCMeta, abstractmethod
from persistent import Persistent

class Ficha(metaclass=ABCMeta):
    '''Clase abstracta Ficha'''
    #Variable de clase
    cliente = []
    @abstractmethod
    def __init__(self):
        pass

class Recibo(Ficha):
    '''Clase Recibo'''
    #Variable de clase
    dispositivo = []
    def __init__(self, fecha, presupuesto, validez, tecnico, observacion, dispositivo):
        self.fecha = fecha
        self.presupuesto = presupuesto
        self.validez = validez
        self.tecnico = tecnico
        self.observacion = observacion
        self.dispositivo = dispositivo
        #self.dispositivo.append(dispositivo)