# from sistema.Empresa import *
import sys
import os
# ruta = os.getcwd()
# sys.path.insert(0, ruta+'sgree')
from controller import *
from empresa import *


c = Controller()
c.crear_recibo()
# c.agregar_cliente()
# c.listar_clientes()
# c.imprimir_recibo()
# c.buscar_recibo()
# c.editar_recibo()
# c.listar_recibos()