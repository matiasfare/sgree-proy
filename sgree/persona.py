#-----------------------------------PERSONA-------------------------------------------------
from abc import ABCMeta, abstractmethod
from persistent import Persistent

class Persona(metaclass=ABCMeta):
    '''Clase Abstracta persona'''
    clave = 'Persona'
    @abstractmethod
    def __init__ (self, documento, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
    def getClave(self):
        pass

class Cliente(Persona,Persistent):
    '''Clase para crear un Cliente'''
    tipo = "Clientes"
    contacto = []
    
    def getClave(self):
        return self.clave

    def __init__(self, documento, nombre, apellido, contacto):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.contacto = contacto

class Tecnico(Persona,Persistent):
    '''Clase para un Tecnico'''
    tipo = "Tecnicos"
    
    def __init__(self, documento, nombre, apellido,contacto, dispositivos):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.contacto = contacto
        self.dispositivos = dispositivos
    
    def getClave(self):
        return self.tipo