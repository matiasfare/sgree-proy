#-----------------------------------MODEL-------------------------------------------------
#Model.py
import os
import pickle
from sgree.persona import Persona
from sgree.ficha import Recibo

class Model():

    def guardar_recibo(self, recibo):
        result = []
        if os.path.getsize(recibo) > 0:
            #lee el archibo recibo
            archivo = open('recibo.pickle', 'rb')
            #carga el carchivo recibo
            result = pickle.load(archivo)
            #cierra, nose para que
            archivo.close()
            #crea el archivo recibo
            archivo_nuevo = open('recibo.pickle','wb')
            #carga el nuevo objeto en memoria
            result.append(archivo_nuevo)
            # Escribe objero en archivo
            pickle.dump(result, archivo_nuevo)
            # Cierra archivo
            archivo_nuevo.close()
        else: #en caso que el archivo no exista
            #crea el archivo recibo
            archivo_nuevo = open('recibo.pickle','wb')
            #carga el nuevo objeto en memoria
            result.append(recibo)
            # Escribe objero en archivo
            pickle.dump(result, archivo_nuevo)
            # Cierra archivo
            archivo_nuevo.close()
        return

    def guardar_persona(self, cliente):
        result = []

        if os.path.getsize(cliente) > 0:
            archivo = open('cliente.pickle', 'rb')
            result = pickle.load(archivo)
            archivo.close()
            archivo_nuevo = open('cliente.pickle','wb')
            result.append(persona)
            pickle.dump(result, archivo_nuevo)
            archivo_nuevo.close()
        else:
            archivo_nuevo = open('cliente.pickle','wb')
            result.append(persona)
            pickle.dump(result, archivo_nuevo)
            archivo_nuevo.close()
        return
        
    def listar_personas(self):
        result = []
        try:
            archivo = open('persona.pickle','rb')
            result = pickle.load(archivo)
            archivo.close()
            return result
        except IOError:
            return result 
        return
        
    def buscar_por_cedula(self, cedula):
        '''Busca Cliente en la bd por cedula, si ese no exites retorna un mensaje'''
        no_encontrado = "Cliente no Encontrado"
        try:
            archivo = open('cliente.pickle','rb')
            lista_clientes = pickle.load(archivo)
            archivo.close()
            for cliente in lista_clientes:
                if(cliente.documento == cedula):
                    resultado = {"Nombre ": cliente.nombre, "Apellido ": Cliente.apellido, "Contacto ": cliente.contacto}
                    return resultado
            return no_encontrado
        except IOError:
            return no_encontrado 
        return

    def listar_recibos(self):
        result = []
        try:
            archivo = open('recibo.pickle','rb')
            result = pickle.load(archivo)
            archivo.close()
            return result
        except IOError:
            return result 
        return



