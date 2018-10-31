#-----------------------------------MODEL-------------------------------------------------
#Model.py
import sys
import os
ruta = os.getcwd()
sys.path.insert(0, ruta+'sgree')
#importa libreria Pickle basada hecha en C
from sgree.myzodb import MiZODB, transaction
import persistent
from persona import Cliente


class Model():
       
    def persistir_objeto(self,objeto, key):
        db = MiZODB('sgree-data.fs')
        dbroot[key] = objeto
        transaction.commit()
        db.close()
        
    
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

    def listar_recibos(self,key):
        '''Retorna todos los objetos que pertenezcan a la key'''
        dbroot = db.raiz
        print (key + ' :', dbroot[key])
        return dbroot[key]

    def editar(self):
        '''Debe restortar el elemento a editar'''
        pass
        
         



db = MiZODB('./sgree/data/sgree-data.fs')
dbroot = db.raiz
modulos= ["empresa","sucursal","dispositivo","ficha","recibo","persona","cliente","tecnico","personal","contacto","pc","celular","notebook"]
for i in modulos:
    try:
        #print(i)
        if not str(i) in dbroot:
            dbroot[i] = {}
    except KeyError:
        print("clave invalida")

c = Model()

a = c.getAll()

print (a)