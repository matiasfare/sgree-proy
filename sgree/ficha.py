#-----------------------------------FICHA-------------------------------------------------

from abc import ABCMeta, abstractmethod
from persistent import Persistent
from datetime import datetime, date, time, timedelta
import calendar

class Ficha(metaclass=ABCMeta):
    '''Clase abstracta Ficha'''
    #Variable de clase
    cliente = []
    @abstractmethod
    def __init__(self):
        pass

class Recibo(Ficha,Persistent):
    '''Clase Recibo'''
    #Variable de clase
    tipo = "Recibos"
    dispositivo = []

    def get_clave(self):
        return self.tipo
    

    def __init__(self, fecha, presupuesto, validez, tecnico, observacion, dispositivo,cliente,estado):
        self.fecha = fecha
        self.presupuesto = presupuesto
        self.validez = validez
        self.tecnico = tecnico
        self.observacion = observacion
        self.dispositivo = dispositivo
        self.cliente = cliente
        self.estado = estado
        #self.dispositivo.append(dispositivo)
    
    def calcular_validez(self):
        #formato de la fecha
        formato_fecha = "%Y-%m-%d"
        #Cambia formato de la fecha
        print('Fecha Recibo: '+self.fecha)
        print('Validez: '+self.validez)
        fecha = datetime.strptime(self.fecha, formato_fecha).date()
        
        fecha_rec = fecha + timedelta(days = int(self.validez))
        print("\tFecha Vencimiento Recibo:", fecha_rec)
        #Fecha Actual
        fecha_act = date.today()
        #Si el recibo es valido resul = True
        resul = (fecha_rec >= fecha_act)
        print("\tEs valido el Recibo:", resul)
        return resul
