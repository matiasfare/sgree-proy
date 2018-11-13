#-----------------------------------PERSONA-------------------------------------------------
from abc import ABCMeta, abstractmethod
from persistent import Persistent

class Persona(metaclass=ABCMeta):
    '''Clase Abstracta persona'''
    @abstractmethod
    def __init__ (self, documento, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

class Cliente(Persona,Persistent):
    '''Clase para crear un Cliente'''
    tipo = "cliente"
    contacto = []
    def __init__(self, documento, nombre, apellido, contacto):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.contacto.append(contacto)

class Tecnico(Persona):
    '''Clase para un Tecnico'''
    tipo = "tecnico"
    def __init__(self, documento, nombre, apellido,contacto, dispositivos):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.contacto = contacto
        self.dispositivos = dispositivos