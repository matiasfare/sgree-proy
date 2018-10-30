
# from Empresa import *
# import persistent, os

# storage = FileStorage.FileStorage("datasys/sgree-data.fs")
# db = DB(storage)
# connection = db.open()
# root = connection.root

import sys, os
 
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
    print ("----------MENU LISTAR RECIBO-------------!\n")
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
    os.system('clear')
    print('Indique lo que desera realizar:')
    print('--------------------------------')
    print('Crear Recibo (1)')
    print('Buscar       (2)')
    print('Listar       (3)')
    print('Editar Fiopa (4)')
    print ("\nSalir (0)")
    opcion = input(" >>  ")
    exec_menu(opcion)
 
    return
 
# Execute menu
def exec_menu(opcion):
    os.system('clear')
    op = opcion
    if op == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[op.lower()]()
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
    '9': back,
    '0': exit,
}
 
# =======================
#      MAIN PROGRAM
# =======================
 
# Main Program
if __name__ == "__main__":
    # Lanza el menu
    main_menu()

db.close()