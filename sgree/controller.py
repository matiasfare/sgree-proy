# -*- coding: utf-8 -*-
#-----------------------------------CONTROLLER-------------------------------------------------
from sgree.model import Model
from sgree.view import View

class Controller:
        def __init__(self):
            '''Clase controlador De: Modelo y Vista'''
            self.model = Model()
            self.view = View()

        def crear_recibo(self):
            '''Controlador que se comunica con la vista y el modelo para Agregar o Crear Recibo'''
            new_recibo = self.view.vista_crear_recibo()
            recibo = self.model.guardar_recibo(new_recibo)
            self.view.vista_imprimir_recibo_guardado(recibo)

        def agregar_cliente(self):
            '''Controlador que llama al modelo y la vista para agregar un Cliente'''
            cliente = self.view.vista_gregar_cliente()
            self.model.guardar_cliente(cliente)

        def listar_personas(self):
            '''Controlador que se comunica con la vista y el modelo para listar Clientes'''
            listaDePersonas = self.model.listar_personas()
            self.view.vista_listar_persona(lista_de_personas)
            return lista_de_personas

        def buscar_por_cedula(self):
            '''Controlador que se comunica con la vista y el modelo para Buscar Cliente por Cedula'''
            cedula = self.view.vista_buscar_por_cedula()
            respuesta = self.model.buscar_por_cedula(cedula)
            self.view.vista_imprimir_persona_buscada_por_cedula(respuesta)

        def listar_recibos(self):
            '''Imprime Solo Recibos existentes'''
            lista_recibos = self.model.listar_recibos()
            self.view.vista_listar_recibos(lista_recibos)
            return lista_recibos