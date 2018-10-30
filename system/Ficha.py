from abc import ABCMeta, abstractmethod

class Ficha(metaclass=ABCMeta):
    '''Ficha es una clase abstracta'''
    @abstractmethod
    def __init__(self):
        pass

class Recibo(Ficha):
    def __init__(self, fecha, presupuesto, validez, tecnico,dispositivos):
        self.fecha = fecha
        self.presupuesto = presupuesto
        self.validez = validez
        self.tecnico = tecnico
        self.dispositivos = dispositivos

    def crear_recibo():

    	print ('--------------------------CREAR RECIBO----------------------------')
    	cod_cliente = input('Ingrese CI de Cliente')
    	#Se verifica si el cliente existe o no en la BD
    	#exite_cliente(cod_cliente)


    	pass