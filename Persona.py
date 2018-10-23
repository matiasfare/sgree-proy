
class Persona():
    '''Clase Base para una personas'''

    def __init__ (self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula  
    def __str__ (self):
        return (str(self.cedula), self.apellido, self.nombre)

class Cliente(Persona):
    