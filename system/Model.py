#Model.py

import pickle
from Persona import Persona

class Model():

    def guardarPersona(self, persona):
        result = []
        try:
            archivo = open('persona.pickle', 'rb')
            result = pickle.load(archivo)
            archivo.close()
            archivoNuevo = open('persona.pickle','wb')
            result.append(persona)
            pickle.dump(result, archivoNuevo)
            archivoNuevo.close()
        except IOError:
            archivoNuevo = open('persona.pickle','wb')
            result.append(persona)
            pickle.dump(result, archivoNuevo)
            archivoNuevo.close()
        return
        
    def listarPersonas(self):
        result = []
        try:
            archivo = open('persona.pickle','rb')
            result = pickle.load(archivo)
            archivo.close()
            return result
        except IOError:
            return result 
        return
        
    def buscarPorCedula(self, cedula):
        noEncontrado = "Persona no Encontrada"
        try:
            archivo = open('persona.pickle','rb')
            listaPersonas = pickle.load(archivo)
            archivo.close()
            for persona in listaPersonas:
                if(persona.documento == cedula):
                    resultado = {"Nombre ": persona.nombre, "Apellido ": persona.apellido}
                    return resultado
            return noEncontrado
        except IOError:
            return noEncontrado 
        return