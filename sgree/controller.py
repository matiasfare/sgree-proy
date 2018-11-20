# -*- coding: utf-8 -*-
#-----------------------------------CONTROLLER-------------------------------------------------
import model as Model
import view as View
from persistent import Persistent

class Controller(Persistent): 
        def __init__(self):
            '''Clase controlador De: Modelo y Vista'''
            self.model = Model.Model()
            self.view = View.View()
            
            

        # def crear_recibo(self):
        #     '''Controlador que se comunica con la vista y el modelo para Agregar o Crear Recibo'''
        #     new_recibo = self.view.vista_crear_recibo()
        #     recibo = self.model.persistir_objeto(new_recibo,'recibo')
        #     self.vista_imprimir_recibo_guardado(recibo)

        def controll_add_cliente(self):
            '''Controlador que llama al modelo y la vista para agregar un Cliente'''
            cliente = self.view.add_cliente()
            obj = self.model.crear(cliente,'Clientes',cliente.documento)
            print (obj.apellido, obj.nombre, obj.documento, obj.contacto)

        # def listar_clientes(self):
        #     '''Controlador que se comunica con la vista y el modelo para listar Clientes'''
        #     lista = self.model.obtener_lista('Clientes')
        #     self.view.vista_listar(lista)

        # def buscar_por_cedula(self):
        #     '''Controlador que se comunica con la vista y el modelo para Buscar Cliente por Cedula'''
        #     cedula = self.view.vista_buscar_por_cedula()
        #     respuesta = self.model.buscar_por_cedula(cedula)
        #     self.view.vista_imprimir_persona_buscada_por_cedula(respuesta)

        # def listar_recibos(self):
        #     '''Imprime Solo Recibos existentes'''
        #     lista_recibos = self.model.listar_recibos('recibo')
        #     self.vista_listar_recibos(lista_recibos)
        #     return lista_recibos


