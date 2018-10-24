from Ficha import  
from ZODB import FileStorage, DB
from Persona import Cliente
from Dispositivo import Celular, Pc, Notebook


storage = FileStorage.FileStorage("datasys/sgree-data.fs")
db = DB(storage)
connection = db.open()
root = connection.root

class Aplication (persistent.Persistent,Cliente ,Celular):
    
    def imprimir_recibo(self):
        pass



db.close()