#-----------------------------------VIEW-VISTA-------------------------------------------------
#importamos la lib time para obtener time del sistema
import time
import sys, os
from sgree.ficha import *
class View():
        
    def vista_crear_recibo(self):
        '''Intereactua con le usuario asi obtener datos necesarios para crear objeto Recibo '''
        print ("----------CREAR RECIBO-------------!\n")
        fecha = time.strftime("%F")
        print(fecha+"\n")
        dispositivo = input("Ingrese Tipo de Dispositivo: ")
        tecnico = input("Seleccione tecnico: ")
        presupuesto = input("Ingrese Presupuesto(Variable):")
        validez = input("Validez de la Ficha(en dias): ")
        observacion = input("Ingrese Observacion: ")
        nuevo_recibo = Recibo(fecha,presupuesto,validez,tecnico,dispositivo)
        return nuevo_recibo


    def vista_agregar_Cliente(self):
        '''Intereactua con le usuario asi obtener datos necesarios para crear objeto Cliente '''
        print("----------CREAR CLIENTE-------------!\n")
        cedula  = input("Ingrese documento del nuevo Cliente: ")
        nombre = input("Ingrese el nombre del nuevo Cliente:")
        apellido = input("ingrese el apellido del nuevo Cliente:")
        contacto = input ("Ingrese numero de contacto: ")
        nuevo_cliente = Cliente(cedula, nombre, apellido, contacto)
        return nuevo_cliente


    def vista_listar_persona(self, lista_cliente):
        print('Listado de personas en la base de datos: \n')
        if lista_cliente:
            for persona in lista_cliente:
                print('Nombre: ', Cliente.nombre, ', Apellido: ', Cliente.apellido, ', Documento: ', Cliente.documento)


    def vista_listar_recibos(self, lista_recibo):
        print('Listado de Recibos en la base de datos: \n')
        if lista_recibo:
            for Recibo in lista_recibo:
                print('Fecha: ', Recibo.fecha, '\n Presupuesto : ', Recibo.validez, 'dias', ',\n Tecnico: ', Recibo.tecnico)


    def vista_buscar_por_cedula(self):
        cedula = input("Ingrese el numero de documento de la persona a buscar: ")
        return cedula


    def vista_imprimir_persona_buscada_por_cedula(self, resultado):
        print("La persona encontrada es: ", resultado)


    def vista_imprimir_recibo_guardado(self, resultado):
        print("El recibo creado es: ", resultado)


    def selecionar_tecnico(self):
        '''selecciona tenico para la ficha
        busca en la bd, si el tecnico seleccionado existe o no'''
        op = opcion.lower()

        return op



    

#     # Menu 2
#     def buscar_recibo():
#         print ("----------MENU BUSCAR RECIBO-------------!\n")
#         print ("9. Back")
#         print ("0. Quit") 
#         opcion = input(" >>  ")
#         exec_menu(opcion)
#         return


#     # Menu 3
#     def listar_recibo():
#         print ("----------MENU LISTAR-------------!\n")
#         print ("9. Back")
#         print ("0. Quit") 
#         opcion = input(" >>  ")
#         exec_menu(opcion)
#         return


#     # Menu 4
#     def editar_ficha():
#         print ("----------MENU EDITAR RECIBO-------------!\n")
#         print ("9. Back")
#         print ("0. Quit") 
#         opcion = input(" >>  ")
#         exec_menu(opcion)
#         return

#     # Back al menu principal
#     def back():
#         menu_actions['main_menu']()
 
#     # Exit program
#     def exit():
#         sys.exit()

#     # Main definition - constante
#         menu_actions  = {}  
 
#     # Main menu
#     def main_menu():   
#         #os.system('clear')
#         print('Indique lo que desera realizar:')
#         print('--------------------------------')
#         print('Crear Recibo   (1)')
#         print('Buscar         (2)')
#         print('Listar Cliente (3)')
#         print('Editar Ficha   (4)')
#         print('Agregar Persona(5)')
#         print ("\nSalir (0)")
#         opcion = input(" >>  ")
#         exec_menu(opcion) 
#         return
 
#     # Execute menu
#     def exec_menu(opcion):
#         '''Verifica que la opcion ingresada sea la correcta, de no ser asi vuelve a solcitar opcion'''
#         os.system('clear')
#         #print('Se verifica que la opcion ingresada sea la correcta, de no ser asi vuelve a solcitar opcion\n')
#         op = opcion.lower()
#         if op == '':
#             menu_actions['main_menu']()
#         else:
#             try:
#                 menu_actions[op]()
#             except KeyError:
#                 print ("Invalid selection, please try again.\n")
#                 menu_actions['main_menu']()
#         return
 
# # =======================
# #    MENUS DEFINITIONS
# # =======================
 
# # Menu definition
#     menu_actions = {
#        'main_menu': main_menu,
#        '1': crear_recibo,
#        '2': buscar_recibo,
#        '3': listar_recibo,
#        '4': editar_ficha,
#        '5': agregar_persona,
#        '9': back,
#        '0': exit,
#     }


# main_menu()