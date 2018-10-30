#view.py

from Persona import Persona
import sys, os
class View():
    
    def vista_agregar_persona(self):
        print("Crear una nueva persona:")
        cedula  = input("Ingrese documento de la nueva persona: ")
        nombre = raw_input("Ingrese el nombre de la nueva persona:")
        apellido = raw_input("ingrese el apellido de la nueva persona:")
        nuevaPersona = Persona(cedula, nombre, apellido)
        return nuevaPersona

    def vista_listar_persona(self, listaPersonas):
        print('Listado de personas en la base de datos: \n')
        if listaPersonas:
            for persona in listaPersonas:
                print('Nombre: ', persona.nombre, ', Apellido: ', persona.apellido, ', Documento: ', persona.documento)

    def vista_buscar_por_cedula(self):
        cedula = input("Ingrese el numero de documento de la persona a buscar: ")
        return cedula

    def vista_imprimir_persona_buscada_por_cedula(self, resultado):
        print("La persona encontrada es: ", resultado)


 
# Menu 1
def crear_recibo():
    print ("----------MENU CREAR RECIBO-------------!\n")
    print ("9. Back")
    print ("0. Quit") 
    opcion = input(" >>  ")
    exec_menu(opcion)
    return

# Menu 2
def buscar_recibo():
    print ("----------MENU BUSCAR RECIBO-------------!\n")
    print ("9. Back")
    print ("0. Quit") 
    opcion = input(" >>  ")
    exec_menu(opcion)
    return


# Menu 3
def listar_recibo():
    print ("----------MENU LISTAR-------------!\n")
    print ("9. Back")
    print ("0. Quit") 
    opcion = input(" >>  ")
    exec_menu(opcion)
    return


# Menu 4
def editar_ficha():
    print ("----------MENU EDITAR RECIBO-------------!\n")
    print ("9. Back")
    print ("0. Quit") 
    opcion = input(" >>  ")
    exec_menu(opcion)
    return

# Back al menu principal
def back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    sys.exit()

# Main definition - constante
menu_actions  = {}  
 
# Main menu
def main_menu():   
    #os.system('clear')
    print('Indique lo que desera realizar:')
    print('--------------------------------')
    print('Crear Recibo   (1)')
    print('Buscar         (2)')
    print('Listar Cliente (3)')
    print('Editar Ficha   (4)')
    print ("\nSalir (0)")
    opcion = input(" >>  ")
    exec_menu(opcion)
 
    return
 
# Execute menu
def exec_menu(opcion):
    '''Verifica que la opcion ingresada sea la correcta, de no ser asi vuelve a solcitar opcion'''
    os.system('clear')
    #print('Se verifica que la opcion ingresada sea la correcta, de no ser asi vuelve a solcitar opcion\n')
    op = opcion.lower()
    if op == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[op]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return
 
# =======================
#    MENUS DEFINITIONS
# =======================
 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': crear_recibo,
    '2': buscar_recibo,
    '3': listar_recibo,
    '4': editar_ficha,
    '4': agregar_persona,
    '9': back,
    '0': exit,
}

 
main_menu()