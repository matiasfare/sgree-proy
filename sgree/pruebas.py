class Cliente():
    '''Clase para crear un Cliente'''
    tipo = "cliente"
    contactos = []
    def __init__(self, documento, nombre, apellido, contacto):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.contacto = contacto



diccionarios = {
    'clientes': {},
    'recibos': {}
}

dbroot = {'dicc': diccionarios}

cliente1 = Cliente(5749,'Matias','Fare', '0981135750')
cliente2 = Cliente(5748,'Anibal','Fare', '0981135750')

dic_actual = dbroot['dicc']

dic_actual = dic_actual['clientes'] 

dic_actual[cliente1.documento] = cliente1
dic_actual[cliente2.documento] = cliente2

dic_actual[cliente1.documento] = cliente1



for clave in dic_actual:
    obj = dic_actual[clave]
    print(str(clave) + ":" + obj.nombre + ", " + obj.apellido)





