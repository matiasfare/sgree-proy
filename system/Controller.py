#Controller.py
from Model import Model
from View import View

class Controller:
        def __init__(self):
            self.model = Model()
            self.view = View()

        def agregar_persona(self):
            persona = self.view.vista_gregar_persona()
            self.model.guardar_persona(persona)

        def listar_personas(self):
            listaDePersonas = self.model.listar_personas()
            self.view.vista_listar_persona(listaDePersonas)
            return listaDePersonas

        def buscar_por_cedula(self):
            cedula = self.view.vista_buscar_por_cedula()
            respuesta = self.model.buscar_por_cedula(cedula)
            self.view.vista_imprimir_persona_buscada_por_cedula(respuesta)

main_menu()