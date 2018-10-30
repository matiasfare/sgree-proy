from abc import ABCMeta, abstractmethod

class Dispositivo(metaclass=ABCMeta):
    '''Dispositivo es una clase abstracta'''
    @abstractmethod
    def __init__(self):
        pass

class Celular (Dispositivo):
    pass

class Pc (Dispositivo):
    pass

class Notebook (Dispositivo):
    pass