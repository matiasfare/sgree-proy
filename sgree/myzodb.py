
from ZODB import FileStorage, DB
import transaction
from persistent import Persistent

class MiZODB(object):
    def __init__ (self, archivo):
        self.storage = FileStorage.FileStorage(archivo)
        self.db = DB(self.storage)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()
    
    def close(self):
        self.conexion.close()
        self.db.close()
        self.storage.close()


    def getAll(self):
        db = MiZODB('sgree-data.fs')
        dbroot = db.raiz
        result = []
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, cliente):
                cliente = Cliente(obj.documento, obj.nombre,obj.apellido, obj.contacto)
                result.append(cliente)
        db.close()
        return result


