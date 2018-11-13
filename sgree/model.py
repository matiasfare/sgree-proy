#-----------------------------------MODEL-------------------------------------------------
#Model.py
import sys
import os
from myzodb import MiZODB, transaction
from persistent import Persistent
from persona import Cliente


class Model(Persistent):
       
    def persistir_objeto(self,objeto, key):
        '''Recibe como parametro el objeto y su clave.
        y persiste el obj'''
        db = MiZODB('sgree-data.fs')
        dbroot[key] = objeto
        transaction.commit()
        db.close()

    def listar_recibos(key):
        '''Retorna todos los objetos que pertenezcan a la key'''
        dbroot = db.raiz
        print (key + ' :', dbroot[key])
        return dbroot[key]

    def editar(self):
        '''Debe restortar el elemento a editar'''
        pass
        
       



db = MiZODB('./sgree-data.fs')
dbroot = db.raiz
modulos= ["empresa","sucursal","dispositivo","ficha","recibo","persona","cliente","tecnico","personal","contacto","pc","celular","notebook"]
for i in modulos:
    try:
        #print(i)
        if not str(i) in dbroot:
            dbroot[i] = {}
    except KeyError:
        print("clave invalida")