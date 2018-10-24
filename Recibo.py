#almacena cualquier ficha que se le ingrese
import myzodb

fb = MiDataBase('datos/Data.fs')
dbroot = db.raiz

class Recibo(Ficha):
    def __init__(self, fecha, presupuesto, validez, tecnico,dispositivos):
        self.fecha = fecha
        self.presupuesto = presupuesto
        self.validez = validez
        self.tecnico = tecnico
        self.dispositivos = dispositivos
