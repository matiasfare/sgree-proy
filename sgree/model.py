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
    diccionarios = ['Clientes', 'Recibos','Tecnicos','Contactos']

    def obtener_objetos(self,dic):
        '''Retorna todos los objetos que pertenezcan a la Clave del Diccionario'''
        db = MiZODB('sgree-data.fs')
        dbroot = db.raiz

        if dic in dbroot:
            sub_dic = dbroot[dic]
            resul = copy.copy(sub_dic)
            for key in resul:
                lis = []
                obj = copy.copy(resul[key])
                lis.append(obj)            
        elif not dic in dbroot:
            resul = "La clave es invalida" 
        transaction.commit()
        db.close()
        return resul


    def editar(self):
        '''Debe restortar el elemento a editar'''
        pass


    def guardar(self, obj, clave, dic):
        '''Persiste un objeto, teniendo en cuenta diccionario y clave,objeto al que pertenece'''
        #Abre base de datos  
        db = MiZODB('sgree-data.fs')
        dbroot = db.raiz
        #Si el diccionario no Existe, lo crea y guarda el objeto
        if not dic in dbroot:
            sub_dic = {}
            sub_dic = dbroot[dic]
            sub_dic[clave] = obj
            dbroot[dic] = sub_dic
            resul = True
        #si el dic ya existe, verifica si el dato ya existe, si no es asi, lo guarda
        elif dic in dbroot:
            sub_dic = dbroot[dic]
            if not clave in sub_dic:
                sub_dic[clave] = obj
                dbroot[dic] = sub_dic
                resul = True
            elif clave in sub_dic:
                resul = False
                print ('Ya existe este Dato')
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
        





#---------------------MODEL MVC PRIMER PARCIAL--------------------------------
# model = Model()

# cliente2 = Cliente(57434,'Elias','Fare', '0981135750')

# dic = model.guardar(cliente2,cliente2.documento,'Clientes')


# for clave in dic:
#     obj = dic[clave]
#     print(str(clave) + ":" + obj.nombre + ", " + obj.apellido)

        
# class View():
        
#     def vista_crear_recibo(self):
#         '''Intereactua con le usuario asi obtener datos necesarios para crear objeto Recibo '''
#         print ("----------CREAR RECIBO-------------!\n")
#         fecha = time.strftime("%F")
#         print(fecha+"\n")
#         dispositivo = input("Ingrese Tipo de Dispositivo: ")
#         tecnico = input("Tecnico: ")
#         presupuesto = input("Ingrese Presupuesto(Variable):")
#         validez = input("Validez de la Ficha(en dias): ")
#         observacion = input("Ingrese Observacion: ")
#         nuevo_recibo = Recibo(fecha,presupuesto,validez,tecnico,observacion,dispositivo)
#         return nuevo_recibo


#     def vista_agregar_cliente(self):
#         '''Intereactua con le usuario asi obtener datos necesarios para crear objeto Cliente '''
#         print("----------CREAR CLIENTE-------------!\n")
#         cedula  = input("Ingrese documento del nuevo Cliente: ")
#         nombre = input("Ingrese el nombre del nuevo Cliente:")
#         apellido = input("ingrese el apellido del nuevo Cliente:")
#         contacto = input ("Ingrese numero de contacto: ")
#         nuevo_cliente = Cliente(cedula, nombre, apellido, contacto)
#         return nuevo_cliente


#     def vista_listar(self, lista):
#         '''Recibe como parametro una lista clientes e imprime en pantalla todos sus elementos'''
#         print('Listado de personas en la base de datos: \n')
#         # try:
#         #     for clave in lista:
#         #         obj = lista[clave]
#         #         print('CI: ', clave, ', Apellido: ', obj.apellido, ', Nombre: ', obj.nombre, ', Contacto', obj.contacto, '\n')
#         # except KeyError:
#         #     print("Error de Clave")
#         for clave in lista:
#             print (clave, ":", lista[clave].nombre, ", ", lista[clave].apellido)

                   


#     # def vista_listar_recibos(self, lista_recibo):
#     #     '''Recibe como parametro la lista de recibos e imprime en pantalla'''
#     #     print('Listado de Recibos en la base de datos: \n')
#     #     if lista_recibo:
#     #         for Recibo in lista_recibo[]:
#     #             print('Fecha: ', Recibo.fecha, '\n Presupuesto : ', Recibo.validez, 'dias', ',\n Tecnico: ', Recibo.tecnico)


#     def vista_buscar_por_cedula(self):
#         '''Pide al usuario ingresar el numero de documento a buscar'''
#         cedula = input("Ingrese el numero de documento de la persona a buscar: ")
#         return cedula


#     def vista_imprimir_persona_buscada_por_cedula(self, resultado):
#         '''Recibe como paremetro el resultado de la busqueda e imprime en pantalla'''
#         print("La persona encontrada es: ", resultado)


#     def vista_imprimir_recibo(self, resultado):
#         '''Recibe como paremetro un objeto Recibo e imprime en pantalla'''
#         print("El recibo creado es: ", resultado)


#     # def selecionar_tecnico(self):
#     #     '''selecciona tenico para la ficha busca en la bd.
#     #      si el tecnico seleccionado existe o no, en caso que exista lo retorna'''
#     #     listar_tecnicos()
#     #     op = input_entero()
#     #     # try op =! int:
#     #     #     op = lee_entero()
#     #     # else:
#     #     # pass
#     #     return op



