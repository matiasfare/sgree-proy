
class Persona():
    '''Clase Base para una personas'''

    def __init__ (self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula  
    # def __str__ (self):
    #     return (str(self.cedula), self.apellido, self.nombre)


class Cliente(Persona):
    '''Clase para un Cliente'''
    tipo = "cliente"
    def __init__(self, nombre, apellido, cedula, contacto, dispositivos):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.contacto = contacto
        self.dispositivos = dispositivos
        
        #return (str(self.cedula), self.apellido, self.nombre, self.contacto, self.dispositivos)

class Tecnico(Persona):
    '''Clase para un Cliente'''
    tipo = "tecnico"
    def crear_cliente(self, nombre, apellido, cedula, contacto, dispositivos):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.contacto = contacto
        self.dispositivos = dispositivos
        
        return (str(self.cedula), self.apellido, self.nombre, self.contacto, self.dispositivos)

