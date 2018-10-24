from abc import ABCMeta, abstractmethod

class Ficha(metaclass=ABCMeta):
    '''Ficha es una clase abstracta'''
    @abstractmethod
    def __init__(self):
        pass