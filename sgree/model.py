import sys
import os
from myzodb import MiZODB, transaction
import persistent
from persona import Cliente
import copy

import time
import sys, os
from ficha import Recibo
from persona import Cliente,Tecnico


class Model(persistent.Persistent):
    diccionarios = ['Clientes', 'Recibos','Tecnicos']

    @staticmethod
    def obtener_objetos(self):
        '''Retorna todos los objetos que pertenezcan a la Clave del Diccionario'''
        db = MiZODB('sgree-data.fs')
        dbroot = db.raiz
        lista = []
        for i in dbroot[self.get_clave(self)]:
            lista.append(copy.copy(i))
        transaction.commit()
        db.close()
        return lista


    def guardar(self, obj, dic):
        '''Persiste un objeto, teniendo en cuenta diccionario y clave,objeto al que pertenece'''
        #Abre base de datos  
        db = MiZODB('sgree-data.fs')
        dbroot = db.raiz
        #Si el diccionario no Existe, lo crea y guarda el objeto
        try:
            if not dic in dbroot:
                sub_lis = []
                dbroot[dic] = sub_lis
                sub_lis.append(obj)
                dbroot[dic] = sub_lis
                resul = True
            #si el dic ya existe, verifica si el dato ya existe, si no es asi, lo guarda
            elif dic in dbroot:
                sub_lis = dbroot[dic]
                if not obj in sub_lis:
                    sub_lis.append(obj)
                    dbroot[dic] = sub_lis
                    resul = True
        except AttributeError as e:
            resul = e
        transaction.commit()
        db.close()
        return resul


    def eliminar_obj(self,clave, dic):
        '''Elimina un objeto, teniendo en cuenta diccionario y clave al que pertenece'''
        MiZODB('sgree-data.fs').close()
        #Abre base de datos  
        db = MiZODB('sgree-data.fs')
        dbroot = db.raiz
        # verifica que exista el diccionario
        # Si el diccionario existe borra la clave, si esta existe
        if dic in dbroot:
            sub_dic = dbroot[dic]
            print(sub_dic)
            if  clave in sub_dic:
                del sub_dic[clave]
                dbroot[dic] = sub_dic
                resul = True
            elif not clave in sub_dic:
                resul = False
                print ('No existe este Dato')
        transaction.commit()
        db.close()
        return resul

    def update(self, obj,indice):
        '''Actualiza un objeto, teniendo en cuenta diccionario y clave'''
        #Abre base de datos  
        db = MiZODB('sgree-data.fs')
        dbroot = db.raiz
        dic = obj.get_clave()

        if dic in dbroot:
            sub_lis = dbroot[dic]
            sub_lis[indice] = obj
            dbroot[dic] = sub_lis
            resul = True
        else:
            resul = False
            
        transaction.commit()
        db.close()
        return resul



