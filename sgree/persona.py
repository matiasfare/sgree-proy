#-----------------------------------PERSONA-------------------------------------------------
from abc import ABCMeta, abstractmethod


class Persona(metaclass=ABCMeta):
    '''Clase Abstracta persona'''
    @abstractmethod
    def __init__ (self, documento, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

class Cliente(Persona):
    '''Clase para crear un Cliente'''
    tipo = "cliente"
    def __init__(self,documento, nombre, apellido,contacto):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.contacto = contacto
        self.dispositivos = dispositivos

class Tecnico(Persona):
    '''Clase para un Tecnico'''
    tipo = "tecnico"
    def crear_cliente(self, nombre, apellido, cedula, contacto, dispositivos):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.contacto = contacto
        self.dispositivos = dispositivos